import json
from datetime import datetime
from time import sleep
from random import choice
from kafka import KafkaProducer
from database import extract_data, create_connection

#create db connection
conn = create_connection()

# Extract data from the database and convert to JSON
database_data = json.loads(extract_data(conn))
print("database_data==", type(database_data))

kafka_server = ["localhost:9092"]
topic = "my-topic-rk"

def get_producer_connection():
    try:
        producer = KafkaProducer(
            bootstrap_servers=kafka_server,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        return True, producer
    except Exception as e:
        print("error_in producer :", e)
        return False, None


def produce_messages(producer):
    while True:
        for data in database_data:
            print(data)
            producer.send(topic, data)
            producer.flush()
            sleep(3)


print("Connecting with Kafka_Producer")
status, producer = get_producer_connection()
if status:
    print("Connection Made with kafka_Producer___")
    produce_messages(producer)
else:
    print("exiting Unable to connection with kafka Producer")


