from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from bot import bot
from strings.game_strings import game_strings
from strings.errors import error_strings
from db.db_requests import check_user_exists
from keyboards.prebuilt import close_kb
from game.play.get_random_word import get_random_word

router = Router()


@router.message(Command("play"))
async def play(message: Message, state: FSMContext):
    await message.delete()
    if await check_user_exists(message.from_user.id):
        msg = await bot.send_message(
            chat_id=message.chat.id,
            text=game_strings["play_start"],
        )
        word = await get_random_word()
        await state.update_data(tries_left=6, word=word, guesses=[msg.message_id])
        await state.set_state("playing")
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=error_strings["user_not_exist"],
            reply_markup=close_kb
        )
