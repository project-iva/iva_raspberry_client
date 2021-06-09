import asyncio
import websockets
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
    uri = "ws://localhost:5678/raspberry"
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            message = RaspberryWebSocketMessage.from_json(message)
            handle_message(message)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(handle_websocket())
