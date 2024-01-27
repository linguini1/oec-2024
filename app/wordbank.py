import random
from typing import TypeAlias

WordBank: TypeAlias = dict[str, str]

ANIMALS: WordBank = {
    "rabbit": "",
    "hedgehog": "",
    "koala": "",
    "kangaroo": "",
    "polar bear": "",
    "cheetah": "",
    "platypus": "",
}

FRUITS: WordBank = {
    "watermelon": "",
    "apple": "",
    "banana": "",
    "strawberry": "",
    "oranges": "",
    "pineapple": "",
}


def choose_random(wordbank: WordBank) -> (str, str):
    """Returns a random word from the word bank and the file path of its associated image."""
    key: str = random.choice(list(wordbank.keys()))
    return key, wordbank[key]
