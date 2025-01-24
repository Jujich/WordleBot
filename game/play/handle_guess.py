from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from strings.game_strings import game_strings_en, game_strings_ru
from keyboards.prebuilt import close_kb_en, close_kb_ru
from bot import bot
from db.db_requests import (increment_user_lose,
                            increment_user_win,
                            increment_user_streak,
                            reset_user_streak,
                            increment_user_daily_lose,
                            increment_user_daily_win,
                            get_user_language)
from game.rules import rules
from game.stats.stats import stats

router = Router()


@router.message(StateFilter("playing_daily"))
@router.message(StateFilter("playing"))
async def handle_guess(message: Message, state: FSMContext):
    await message.delete()
    lang = await get_user_language(message.from_user.id)
    strings = game_strings_en if lang == "en" else game_strings_ru
    kb = close_kb_en if lang == "en" else close_kb_ru
    state_data = await state.get_data()
    guesses = state_data["guesses"]

    if message.text == "/rules":
        await rules(message)
        return
    if message.text == "/stats":
        await stats(message)
        return
    if message.text in ["/play", "/settings", "/daily"]:
        msg = await message.answer(
            text=strings["game_already_started"],
        )
        guesses.append(msg.message_id)
        await state.update_data(guesses=guesses)
        return
    if message.text == "/stop":
        await message.answer(
            text=strings["game_stopped"],
            reply_markup=kb
        )
        for message_id in state_data["guesses"]:
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message_id
            )
        await state.clear()
        return

    words = state_data["words"]
    word = state_data["word"]
    tries_left = state_data["tries_left"]
    guess = message.text.lower()
    state_ = await state.get_state()

    if len(guess) != 5:
        msg = await message.answer(strings["guess_wrong_length"])
        guesses.append(msg.message_id)
        await state.update_data(guesses=guesses)
        return

    tiles = await count_tiles(guess, word)

    if guess not in words:
        msg = await message.answer(strings["not_a_word"].substitute(guess=guess))
        guesses.append(msg.message_id)
        await state.update_data(guesses=guesses)
        return

    if guess == word:
        for message_id in state_data["guesses"]:
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message_id
            )
        await message.answer(
            text=strings["correct_guess"].substitute(word=guess),
            reply_markup=kb)
        if state_ == "playing_daily":
            await increment_user_daily_win(message.from_user.id)
            await increment_user_streak(message.from_user.id)
        else:
            await increment_user_win(message.from_user.id)
        await state.clear()
        return

    if tries_left == 1:
        for message_id in state_data["guesses"]:
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message_id
            )
        await message.answer(
            strings["out_of_tries"].substitute(word=word),
            reply_markup=kb
        )
        if state_ == "playing_daily":
            await increment_user_daily_lose(message.from_user.id)
            await reset_user_streak(message.from_user.id)
        else:
            await increment_user_lose(message.from_user.id)
        await state.clear()
        return

    if state_data["max_tries"] == "∞":
        pass
    else:
        tries_left -= 1
    msg = await message.answer(strings["wrong_guess"].substitute(
        tries_left=tries_left,
        tries=state_data["max_tries"],
        guess="<b>  " + "  ".join(guess) + "</b>",
        tiles="".join(tiles)
    ))
    guesses.append(msg.message_id)
    await state.update_data(tries_left=tries_left, guesses=guesses)


async def count_tiles(guess: str, word: str) -> list[str]:
    tiles = []
    letters = []
    for i, letter in enumerate(guess):
        if letter in letters and word.count(letter) <= 1:
            tiles.append("⬜️")
        elif letter == word[i]:
            tiles.append("🟩")
        elif letter in word:
            tiles.append("🟨")
        else:
            tiles.append("⬜️")
        letters.append(letter)
    return tiles
