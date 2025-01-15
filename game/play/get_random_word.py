import random

with open("game/play/words.txt", "r") as f:
    words = f.read().splitlines()


async def get_random_word() -> str:
    return random.choice(words)
