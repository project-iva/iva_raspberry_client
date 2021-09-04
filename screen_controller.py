import os
from enum import Enum


class ScreenController:
    class Action(str, Enum):
        SCREEN_ON = 'screen_on'
        SCREEN_OFF = 'screen_off'

    @staticmethod
    def handle_action(action: Action):
        dispatcher = {
            ScreenController.Action.SCREEN_ON: ScreenController.turn_screen_on,
            ScreenController.Action.SCREEN_OFF: ScreenController.turn_screen_off
        }

        # perform action
        dispatcher[action]()

    @staticmethod
    def turn_screen_on():
        print('turning screen on')
        os.system('vcgencmd display_power 1')

    @staticmethod
    def turn_screen_off():
        print('turning screen off')
        os.system('vcgencmd display_power 0')
