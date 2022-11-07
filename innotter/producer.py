import os

import pika, json

params = pika.URLParameters('amqps://qqrcvbgr:Ptu8OHLHnbTjVG2SoNSxVAuQoZaqC9VE@moose.rmq.cloudamqp.com/qqrcvbgr')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(body):
    channel.basic_publish(exchange='', routing_key='microservice', body=json.dumps(body))
