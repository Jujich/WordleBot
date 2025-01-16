from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router
from db.db_requests import (get_user_settings,
                            check_user_exists,
                            get_daily_words,
                            played_daily_set,
                            check_played_daily)
from strings.game_strings import game_strings_en, game_strings_ru
from strings.errors import error_strings_en, error_strings_ru
from keyboards.prebuilt import close_kb_en, close_kb_ru
from bot import bot
from game.play.get_random_word import get_words

router = Router()


@router.message(Command("daily"))
async def play_daily(message: Message, state: FSMContext):
    await message.delete()
    state_ = await state.get_state()
    state_data = await state.get_data()
    user_settings = await get_user_settings(message.from_user.id)
    language = user_settings["language"]
    strings = game_strings_en if language == "en" else game_strings_ru
    err_strings = error_strings_en if language == "en" else error_strings_ru
    kb = close_kb_en if language == "en" else close_kb_ru
    if await check_user_exists(message.from_user.id):
        completed_daily = await check_played_daily(message.from_user.id)
        if completed_daily:
            await message.answer(
                text=strings["daily_completed"],
                reply_markup=kb
            )
            return
        if state_ == "playing_daily":
            guesses = state_data["guesses"]
            msg = await message.answer(
                text=strings["game_already_started"],
            )
            guesses.append(msg.message_id)
            await state.update_data(guesses=guesses)
            return

        daily_words = await get_daily_words()
        if not daily_words:
            await bot.send_message(
                chat_id=message.chat.id,
                text=err_strings["daily_not_exist"],
                reply_markup=kb
            )
            return
        daily = daily_words["word_en"] if language == "en" else daily_words["word_ru"]
        words = await get_words(language)
        msg = await message.answer(
            text=strings["play_daily"],
        )

        await state.update_data(
            max_tries=6,
            tries_left=6,
            words=words,
            word=daily,
            guesses=[msg.message_id]
        )

        await played_daily_set(message.from_user.id)

        await state.set_state("playing_daily")
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=err_strings["user_not_exist"],
            reply_markup=kb
        )
