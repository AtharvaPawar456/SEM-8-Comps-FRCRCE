import pika
from mock import Mock
import time

# Declare a direct exchange named 'jobs'
# (Note: Declare the exchange and queue in the simulated RabbitMQ server script)

# Mock the call to `pika.BlockingConnection` in the simulated RabbitMQ server script
mocked_connection = Mock()
mocked_channel = Mock()
mocked_channel.basic_publish.return_value = None
mocked_connection.channel.return_value = mocked_channel
pika.BlockingConnection.return_value = mocked_connection

# Publish a message to the 'jobs' exchange with a routing key 'job_queue'
message = "New job: Process data"

print(f" [x] Sent: {message}")

# Adding a slight delay before exiting
time.sleep(1)