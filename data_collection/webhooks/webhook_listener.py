# data_collection/webhooks/webhook_listener.py

import logging
from flask import Flask, request, json, jsonify
import os
# from sqlalchemy import 

app = Flask(__name__)
port = int(os.getenv('PORT', 5000))

# Logging configuration
log_file = os.getenv('LOG_FILE', 'webhook_listener.log')
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler(log_file),
#         logging.StreamHandler()
#     ]
# )

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    if data:
        try:

            filepath = 'webhook_data.json'
            if not os.path.isfile(filepath):
                with open(filepath, 'w') as file:
                    file.write('')

            # Save the incoming data to a file or database

            with open(filepath, 'a') as file:
                file.write(json.dumps(data) + '\n')

            logging.info("Data received and saved")
            return jsonify({'status':'success', 'message':"Data received"}), 200
        
        except Exception as e:
            logging.error(f"Error saving data: {e}")
            return jsonify({"status":"Error", "message":"Internal Server Error"}), 500

    else:
        return jsonify({"status":"Error", "message":f"Fail to fetch the data"}), 400



if '__main__' == __name__:
    app.run(port=port)