

from typing import TypedDict

class Config(TypedDict):
    port: int
    name: str

config: Config = {
    'port': 4000,
    'name': 'David',
    'unknown': True,  # warning, wrong type
}

#port = config["poort"]  # warning, what's a poort?