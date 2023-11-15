import json
from datetime import datetime
from time import sleep
from random import choice
from kafka import KafkaProducer

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
        random_values = [1, 2, 3, 4, 5, 6, 7]
        random_value = choice(random_values)
        data = {
            "test_data": {
                "random_value": random_value
            },
            "timestamp": str(datetime.now()),
            "value_status": "High" if random_value > 5 else "Low"
        }
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


