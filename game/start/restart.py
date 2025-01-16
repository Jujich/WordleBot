from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from bot import bot
from db.db_requests import get_user_language
from strings.menu_strings import menu_strings_en, menu_strings_ru
from keyboards.prebuilt import close_kb_en, close_kb_ru

router = Router()


@router.message(Command("restart"))
async def start(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    lang = await get_user_language(message.from_user.id)
    strings = menu_strings_en if lang == "en" else menu_strings_ru
    kb = close_kb_en if lang == "en" else close_kb_ru
    await bot.send_message(
        chat_id=message.chat.id,
        text=strings["restart"],
        reply_markup=kb
    )
