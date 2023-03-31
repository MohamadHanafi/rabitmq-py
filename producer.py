import pika

# Create a connection to the RabbitMQ server
connectionParameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connectionParameters)

# Create a channel
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='letterbox')

# Send a message
message = 'Hello World!'

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"Sent {message}")

# Close the connection
connection.close()

