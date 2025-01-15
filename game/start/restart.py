from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from bot import bot
from strings.menu_strings import menu_strings
from keyboards.prebuilt import close_kb

router = Router()


@router.message(Command("restart"))
async def start(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    await bot.send_message(
        chat_id=message.chat.id,
        text=menu_strings["restart"],
        reply_markup=close_kb
    )
