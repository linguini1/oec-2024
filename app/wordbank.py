import random
from typing import TypeAlias

WordBank: TypeAlias = dict[str, str]

ANIMALS: WordBank = {
    "rabbit": "static/assets/Rabbit.png",
    "hedgehog": "static/assets/Hedgehog.png",
    "koala": "static/assets/Koala.png",
    "kangaroo": "static/assets/Kangaroo.png",
    "polar bear": "static/assets/PolarBear.png",
    "cheetah": "static/assets/Cheetah.png",
    "platypus": "static/assets/Platypus.png",
}

FRUITS: WordBank = {
    "watermelon": "static/assets/Watermelon.png",
    "apple": "static/assets/Apple.png",
    "banana": "static/assets/Banana.png",
    "strawberry": "static/assets/Strawberry.png",
    "orange": "static/assets/Orange.png",
    "pineapple": "static/assets/Pineapple.png",
}

COUNTRIES: WordBank = {
    "canada": "static/assets/canada.png",
    "haiti": "static/assets/haiti.png",
    "kenya": "static/assets/kenya.png",
    "italy": "static/assets/italy.png",
    "palestine": "static/assets/palestine.png",
}


def choose_random(wordbank: WordBank) -> tuple[str, str]:
    """Returns a random word from the word bank and the file path of its associated image."""
    key: str = random.choice(list(wordbank.keys()))
    return key, wordbank[key]
