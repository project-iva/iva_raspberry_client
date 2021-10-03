import os
from dotenv import load_dotenv
from http_server import run_server

if __name__ == '__main__':
    load_dotenv()

    server_address = os.environ.get('SERVER_ADDRESS', 'localhost')
    server_port = int(os.environ.get('SERVER_PORT', 8000))
    run_server(server_address, server_port)
