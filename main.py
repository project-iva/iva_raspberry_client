import os
from dotenv import load_dotenv
from http_server import run_server
from tts_controller import TTSController

if __name__ == '__main__':
    load_dotenv()

    tts_controller = TTSController()

    server_address = os.environ.get('SERVER_ADDRESS', 'localhost')
    server_port = int(os.environ.get('SERVER_PORT', 8000))
    run_server(server_address, server_port, tts_controller)
