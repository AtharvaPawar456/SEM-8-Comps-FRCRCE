import xmlrpc.client

# Create client
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    # Call remote function
    result = proxy.add(10, 6)
    print(f"Result from remote function: {result}")

