import pika

# Callback function to process received messages
def callback(ch, method, properties, body):
    print(f" [x] Received: {body}")

# Declare a direct exchange named 'jobs'
# (Note: Declare the exchange and queue in the simulated RabbitMQ server script)

# No need to set up the callback function here
# Set up the callback function for incoming messages in the simulated RabbitMQ server script

print(' [*] Waiting for messages. To exit press CTRL+C')
# No need to start consuming here
# channel.start_consuming()
