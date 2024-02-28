# pip install rpyc


import rpyc

# Connect to the RMI server
conn = rpyc.connect("localhost", 8000)

# Get a handle to the remote service
remote_service = conn.root

val1 = 10
val2 = 16

# Call the remote method
result = remote_service.exposed_add_numbers(val1, val2)
print(f"Result from remote method: {val1} + {val2} = {result}")

# Disconnect from the RMI server
conn.close()
