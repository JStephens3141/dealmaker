import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dealmaker.settings")
django.setup()
from leads.models import Lead

params = pika.URLParameters('amqps://sqrszeqh:fPnRCF1Z73IRAp6XH3Fx6x6rSSgCBFcb@cattle.rmq2.cloudamqp.com/sqrszeqh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    lead = Lead.objects.get(id=id)
    lead.propertiesShown = lead.propertiesShown + 1
    lead.save()
    print('Properties Shown Increased')



channel.basic_consume(queue='admin', on_message_callback=callback)

print('started Consuming')

channel.start_consuming()

channel.close()
