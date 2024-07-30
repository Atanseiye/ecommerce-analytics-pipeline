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
                    data = 
                transformed = trasformation(line)

        pass

    except:

        pass

    pass
