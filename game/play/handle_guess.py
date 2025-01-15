from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from strings.game_strings import game_strings
from keyboards.prebuilt import close_kb
from game.play.get_random_word import words
from bot import bot
from db.db_requests import (increment_user_streak,
                            reset_user_streak,
                            increment_user_lose,
                            increment_user_win)
from game.rules import rules
from game.stats.stats import stats

router = Router()


@router.message(StateFilter("playing"))
async def handle_guess(message: Message, state: FSMContext):
    if message.text == "/rules":
        await rules(message, state)
        return
    if message.text == "/stats":
        await stats(message, state)

    state_data = await state.get_data()
    guesses = state_data["guesses"]
    word = state_data["word"]
    tries_left = state_data["tries_left"]
    guess = message.text.lower()
    await message.delete()

    if len(guess) != 5:
        msg = await message.answer(game_strings["guess_wrong_length"])
        guesses.append(msg.message_id)
        await state.update_data(guesses=guesses)
        return

    tiles = []
    for i, letter in enumerate(guess):
        if letter == word[i]:
            tiles.append("🟩")
        elif letter in word:
            tiles.append("🟨")
        else:
            tiles.append("⬜️")

    if guess not in words:
        msg = await message.answer(game_strings["not_a_word"].substitute(guess=guess))
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
            text=game_strings["correct_guess"].substitute(word=guess),
            reply_markup=close_kb)
        await increment_user_win(message.from_user.id)
        await increment_user_streak(message.from_user.id)
        await state.clear()
        return

    if tries_left == 1:
        for message_id in state_data["guesses"]:
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message_id
            )
        await message.answer(
            game_strings["out_of_tries"].substitute(word=word),
            reply_markup=close_kb
        )
        await increment_user_lose(message.from_user.id)
        await reset_user_streak(message.from_user.id)
        await state.clear()
        return

    msg = await message.answer(game_strings["wrong_guess"].substitute(
        tries_left=tries_left - 1,
        guess="<b>  " + "  ".join(guess) + "</b>",
        tiles="".join(tiles)
    ))
    guesses.append(msg.message_id)
    await state.update_data(tries_left=tries_left - 1, guesses=guesses)
