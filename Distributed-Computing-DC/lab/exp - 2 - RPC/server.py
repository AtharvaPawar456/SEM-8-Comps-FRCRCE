from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Example function to be called remotely
    def add(x, y):
        return x + y

    server.register_function(add, 'add')

    # Run the server's main loop
    print("Server is listening on port 8000...")
    server.serve_forever()
