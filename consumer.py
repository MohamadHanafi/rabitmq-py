import pika

credentials = pika.PlainCredentials('queue_demo_chsandbox2','Puo9kR9yv')
parameters = pika.ConnectionParameters('localhost','5672','/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % properties.headers)

channel.basic_consume(queue='queue_demo_chsandbox2', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()