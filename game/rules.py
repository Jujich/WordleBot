from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot import bot
from strings.game_strings import game_strings
from keyboards.prebuilt import close_kb

router = Router()


@router.message(Command("rules"))
async def rules(message: Message):
    await message.delete()
    await bot.send_message(
        chat_id=message.chat.id,
        text=game_strings["rules"],
        reply_markup=close_kb,
    )
