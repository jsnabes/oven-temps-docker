import requests
import datetime
from confluent_kafka import Producer
import time

KAFKA_TOPIC = 'oven'
KAFKA_BOOTSTRAP_SERVERS = 'broker:9092'

oven_readings = 'http://oven:8000'

def delivery_callback(err, msg):
        if err:
                print(f'Message failed delivery: {err}')
        else:
                print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
def main():
        # Kafka producer configuration
        conf = {'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS}
        # Create Kafka producer instance
        producer = Producer(conf)
        start_time = datetime.datetime.now()
        # 20 minute time interval
        time_interval = datetime.timedelta(minutes = 60)
        while True:
            response = requests.get(oven_readings)
            value = response.json()['reading']
            producer.produce(KAFKA_TOPIC, key=None, value = bytes(str(value), encoding='utf-8'), callback=delivery_callback)
            time.sleep(1)
            now = datetime.datetime.now()
            if now - start_time > time_interval:
                break
        # Flush messages to Kafka to ensure they are sent immediately
        producer.flush()
if __name__ == '__main__':
    main()
