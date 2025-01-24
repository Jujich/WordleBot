from aiogram import Router, F
from bot import bot
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "delete_message")
async def delete_message(callback: CallbackQuery):
    await callback.message.delete()
