import json
import datetime, time
from kafka import KafkaConsumer

kafka_topic = "my-topic-rk"
kafka_connection = "localhost:9092"

def get_kafka_connection():
    try:
        consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers=[kafka_connection],
            group_id='my-group-id',
            enable_auto_commit=False,
            max_poll_records=1,
            max_poll_interval_ms=300000,
        )
        return True, consumer
    except:
        return False, None


def consume_messages(consumer):
    while True:
        message_batch = consumer.poll()
        for partition_batch in message_batch.values():
            for message in partition_batch:
                try:
                    # print(message.value)
                    output = message.value  
                    print("output===========", output)
                except Exception as ex:
                    print(ex)
           


print("Connecting with Kafka")
status, consumer = get_kafka_connection()
if status:
    print("Connection Made with kafka")
    consume_messages(consumer)
else:
    print("exiting Unable to connection with kafka")
