from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

from confluent_kafka import Producer
from json import dumps
from time import sleep

import random
import datetime


KAFKA_SERVER = 'kafka-0:9092'
TOPIC_NAME = 'sample-topic'


producer = Producer({
    'bootstrap.servers': KAFKA_SERVER,
    'enable.idempotence': True,
    'acks': 'all',
})

uppercase_letters = "ABCDEFGH"


if __name__ == '__main__':

    admin_client = KafkaAdminClient(
        bootstrap_servers=[KAFKA_SERVER],
        client_id='cid',
    )

    try:
        topic_list = [NewTopic(name=TOPIC_NAME, num_partitions=4, replication_factor=2)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    except TopicAlreadyExistsError:
        pass

    while True:
        random_letter = random.choice(uppercase_letters)
        random_number = random.randint(1, 100)
        data = {'id': random_letter, 'datetime': str(datetime.datetime.now()), 'value': random_number}
        producer.produce(TOPIC_NAME, dumps(data).encode('utf-8'), partition=random.randint(0, 3))
        sleep(random.random()/10)
        producer.flush()
