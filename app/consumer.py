import json
import datetime, time
from kafka import KafkaConsumer
from database import insert_record, create_connection

#create db connection
conn = create_connection()

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
    except Exception as e :
        print("Error_______:", e)
        return False, None


def consume_messages(consumer):
    while True:
        message_batch = consumer.poll()
        for partition_batch in message_batch.values():
            for message in partition_batch:
                try:
                    # print(message.value)
                    output = json.loads(message.value) 
                    data = (output['name'], output['age']) 
                    print("output===========", data)
                    # try  to insert records into db
                    try:
                        insert_record(conn, data)
                    except Exception as e:
                        print("Error:", e)
                        pass
                except Exception as ex:
                    print("Error____", ex)
           


print("Connecting with Kafka")
status, consumer = get_kafka_connection()
if status:
    print("Connection Made with kafka")
    consume_messages(consumer)
else:
    print("exiting Unable to connection with kafka")
