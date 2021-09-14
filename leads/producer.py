import pika, json

params = pika.URLParameters('amqps://sqrszeqh:fPnRCF1Z73IRAp6XH3Fx6x6rSSgCBFcb@cattle.rmq2.cloudamqp.com/sqrszeqh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
