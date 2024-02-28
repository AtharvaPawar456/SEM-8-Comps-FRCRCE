import pika
from mock import Mock

# Mocking pika.BlockingConnection
pika.BlockingConnection = Mock()

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a direct exchange named 'jobs'
channel.exchange_declare(exchange='jobs', exchange_type='direct')

# Declare a queue named 'worker_queue' and bind it to the 'jobs' exchange with a routing key 'job_queue'
channel.queue_declare(queue='worker_queue')
channel.queue_bind(exchange='jobs', queue='worker_queue', routing_key='job_queue')

print(" [*] Simulated RabbitMQ Server is running. Press CTRL+C to exit.")

# Set up the callback function for incoming messages
def callback(ch, method, properties, body):
    print(f" [x] Received: {body}")

channel.basic_consume(queue='worker_queue', on_message_callback=callback, auto_ack=True)

try:
    # Start consuming messages in a loop
    while True:
        connection.process_data_events()
except KeyboardInterrupt:
    print("\n [!] Simulated RabbitMQ Server stopped.")
