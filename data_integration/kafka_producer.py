from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time
from random import randint
import logging




# data transformer
def trasformation():
    pass

############### data producer ###############
def kafka_producer(topic, filepath, bootstrap_servers='localhost:9092'):
    """
    Reads data from a JSON file, transform it and produces message to a kafka topic

    Parameters:
    Topic (str): Kafka topic to produce message to
    file_path (str): filepath to the data that needs to be read to a kafka topic
    boostrap_servers (str): The kafka bootsrap server (default: localhost:9092)
    """

    # initialise the kafka producer client
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        retries=5,  # Retry up to 5 times
        acks='all',  # Wait for all replicas to acknowledge
        buffer_memory=33554432,  # 32 MB buffer
        batch_size=16384,  # 16 KB batch size
    )

    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    transformed = trasformation(data)

                    # Optional: Use a key to ensure data is sent to the same partition
                    key = str(randint(1, 10)).encode('utf-8')

                    # send the data through the producer client
                    producer.send(topic, key=key, value=transformed)
                    logging.info(f"Message sent: {transformed}")
                    time.sleep(10)
                except json.JSONDecodeError as json_err:
                    logging.error(f"Error decoding JSON: {json_err}")
                except KafkaError as kafka_err:
                    logging.error(f"Kafka error: {kafka_err}") 

    except FileNotFoundError as not_found:
        logging.error(f"File not Found: {not_found}")
    except Exception as error:
        logging.info(f"Unexpected error: {error}")

    finally:
        producer.flush()
        producer.close()
        logging.info(f"Data from {filepath} successfully sent to Kafka topic {topic}")
