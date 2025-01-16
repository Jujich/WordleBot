from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from db.db_requests import insert_user, check_user_exists, get_user_language
from bot import bot
from strings.menu_strings import menu_strings_en, menu_strings_ru
from keyboards.prebuilt import close_kb_en, close_kb_ru

router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.delete()
    lang = await get_user_language(message.from_user.id)
    strings = menu_strings_en if lang == "en" else menu_strings_ru
    kb = close_kb_en if lang == "en" else close_kb_ru
    if not await check_user_exists(message.from_user.id):
        await insert_user(message.from_user.id, message.from_user.username)
        await bot.send_message(
            chat_id=message.chat.id,
            text=strings["start"],
            reply_markup=kb
        )
        await state.clear()
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=strings["start_logged"],
            reply_markup=kb
        )
