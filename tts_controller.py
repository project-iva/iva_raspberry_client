from enum import Enum

import pyttsx3


class TTSController:
    class Action(str, Enum):
        SAY = 'SAY'

    def __init__(self):
        self.tts_engine = pyttsx3.init()

    def handle_action(self, action: Action, text: str):
        dispatcher = {
            TTSController.Action.SAY: self.say,
        }
        # perform action
        dispatcher[action](text)

    def say(self, text: str):
        print('saying ', text)
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
