import io
from enum import Enum
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS


class TTSController:
    class Action(str, Enum):
        SAY = 'SAY'

    @staticmethod
    def handle_action(action: Action, text: str):
        dispatcher = {
            TTSController.Action.SAY: TTSController.say,
        }
        # perform action
        dispatcher[action](text)

    @staticmethod
    def say(text: str):
        print(f'saying "{text}"')
        with io.BytesIO() as data:
            gTTS(text=text, lang_check=False).write_to_fp(data)
            data.seek(0)
            speech = AudioSegment.from_file(data, format="mp3")
            play(speech)
