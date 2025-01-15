from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from db.db_requests import insert_user, check_user_exists
from bot import bot
from strings.menu_strings import menu_strings
from keyboards.prebuilt import close_kb

router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.delete()
    if not await check_user_exists(message.from_user.id):
        await insert_user(message.from_user.id, message.from_user.username)
        await bot.send_message(
            chat_id=message.chat.id,
            text=menu_strings["start"],
            reply_markup=close_kb
        )
        await state.clear()
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=menu_strings["start_logged"],
            reply_markup=close_kb
        )
