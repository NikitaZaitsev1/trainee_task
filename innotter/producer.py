import os

import pika, json

params = pika.URLParameters(os.getenv("AMQP_URL"))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(body):
    channel.basic_publish(exchange='', routing_key='microservice', body=json.dumps(body))
