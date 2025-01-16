import random
from game.play.words_ru import words as words_ru

with open("game/play/words_en.txt", "r") as f:
    words_en = f.read().splitlines()


async def get_random_word(language: str) -> str:
    return random.choice(words_en if language == "en" else words_ru)


async def get_words(language: str) -> list[str]:
    return words_en if language == "en" else words_ru
