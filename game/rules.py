from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot import bot
from strings.game_strings import game_strings_en, game_strings_ru
from keyboards.prebuilt import close_kb_en, close_kb_ru
from db.db_requests import get_user_language

router = Router()


@router.message(Command("rules"))
async def rules(message: Message):
    await message.delete()
    lang = await get_user_language(message.from_user.id)
    strings = game_strings_en if lang == "en" else game_strings_ru
    kb = close_kb_en if lang == "en" else close_kb_ru
    await bot.send_message(
        chat_id=message.chat.id,
        text=strings["rules"],
        reply_markup=kb,
    )
