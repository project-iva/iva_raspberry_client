import asyncio
import websockets
from dotenv import load_dotenv

from websocket_message import RaspberryWebSocketMessage, RaspberrySocketMessageAction
import os


def turn_screen_on():
    print('turning screen on')
    os.system('vcgencmd display_power 1')


def turn_screen_off():
    print('turning screen off')
    os.system('vcgencmd display_power 0')


def handle_message(message: RaspberryWebSocketMessage):
    dispatcher = {
        RaspberrySocketMessageAction.SCREEN_ON: turn_screen_on,
        RaspberrySocketMessageAction.SCREEN_OFF: turn_screen_off
    }

    # perform action
    dispatcher[message.action]()


async def handle_websocket():
    iva_websocket_uri = os.environ.get('IVA_WEBSOCKET_URI')
    async with websockets.connect(iva_websocket_uri) as websocket:
        async for message in websocket:
            message = RaspberryWebSocketMessage.from_json(message)
            handle_message(message)


if __name__ == '__main__':
    load_dotenv()
    asyncio.get_event_loop().run_until_complete(handle_websocket())
