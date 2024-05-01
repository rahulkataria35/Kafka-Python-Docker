import json
import time
from kafka import KafkaConsumer
from database import insert_record, create_connection

kafka_topic = "my-topic-rk"
kafka_connection = "kafka:9092"

def get_kafka_connection():
    try:
        time.sleep(5)
        consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers=[kafka_connection],
            group_id='my-group-id',
            enable_auto_commit=False,
            max_poll_records=1,
            max_poll_interval_ms=300000,
        )
        return True, consumer
    except Exception as e:
        print("Error_______:", e)
        return False, None

def consume_messages(consumer, conn):
    for message in consumer:
        try:
            output = json.loads(message.value)
            data = (output['name'], output['age'])
            print("consuming_data------", data)
            try:
                # print("Insert the data again to run the process in loop")
                insert_record(conn, data)
            except Exception as e:
                print("Error:", e)
        except Exception as ex:
            print("Error____", ex)

def start_consumer():
    print("Connecting with Kafka")
    status, consumer = get_kafka_connection()
    if status:
        print("Connection Made with Kafka")
        conn = create_connection()
        consume_messages(consumer, conn)
    else:
        print("Exiting. Unable to connect with Kafka")


print(start_consumer())
