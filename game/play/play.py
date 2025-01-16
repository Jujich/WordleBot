from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from bot import bot
from strings.game_strings import game_strings_en, game_strings_ru
from strings.errors import error_strings_en, error_strings_ru
from db.db_requests import check_user_exists, get_user_settings
from keyboards.prebuilt import close_kb_en, close_kb_ru
from game.play.get_random_word import get_random_word, get_words

router = Router()


@router.message(Command("play"))
async def play(message: Message, state: FSMContext):
    await message.delete()
    state_ = await state.get_state()
    state_data = await state.get_data()
    user_settings = await get_user_settings(message.from_user.id)
    if not user_settings:
        await bot.send_message(
            chat_id=message.chat.id,
            text=error_strings_en["user_not_exist"],
            reply_markup=close_kb_en
        )
    language = user_settings["language"]
    strings = game_strings_en if language == "en" else game_strings_ru

    if state_ == "playing":
        guesses = state_data["guesses"]
        msg = await message.answer(
            text=strings["game_already_started"],
        )
        guesses.append(msg.message_id)
        await state.update_data(guesses=guesses)
        return

    err_strings = error_strings_en if language == "en" else error_strings_ru
    kb = close_kb_en if language == "en" else close_kb_ru
    if await check_user_exists(message.from_user.id):
        if user_settings["tries"] != "inf":
            tries = int(user_settings["tries"])
        else:
            tries = "∞"
        msg = await bot.send_message(
            chat_id=message.chat.id,
            text=strings["play_start"].substitute(tries=tries),
        )
        words = await get_words(language)
        word = await get_random_word(language)
        await state.update_data(
            max_tries=tries,
            tries_left=tries,
            words=words,
            word=word,
            guesses=[msg.message_id]
        )
        await state.set_state("playing")
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=err_strings["user_not_exist"],
            reply_markup=kb
        )
