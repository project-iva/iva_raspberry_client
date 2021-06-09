import json
from dataclasses import dataclass
from enum import Enum


class RaspberrySocketMessageAction(str, Enum):
    SCREEN_ON = 'screen_on'
    SCREEN_OFF = 'screen_off'


@dataclass
class RaspberryWebSocketMessage:
    id: str
    action: RaspberrySocketMessageAction

    @classmethod
    def from_json(cls, j):
        return cls.from_dict(json.loads(j))

    @classmethod
    def from_dict(cls, d):
        return cls(
            d.get('id'),
            RaspberrySocketMessageAction(d.get('action')),
        )
