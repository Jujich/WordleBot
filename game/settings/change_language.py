from aiogram.types import CallbackQuery
from aiogram import Router, F
from strings.menu_strings import menu_strings_en, menu_strings_ru
from db.db_requests import update_user_language, get_user_settings
from keyboards.checked_item_kb import get_user_settings_kb
from bot import bot

router = Router()


@router.callback_query(F.data.regexp(r"language_\w{1,}"))
async def change_language_info(callback: CallbackQuery):
    user_settings = await get_user_settings(callback.from_user.id)
    language = callback.data[9:]
    if await update_user_language(callback.from_user.id, language):
        user_settings["language"] = language
    kb = await get_user_settings_kb(callback.from_user.id)
    text = menu_strings_en["settings"] if user_settings["language"] == "en" else menu_strings_ru["settings"]
    await bot.edit_message_text(
        message_id=callback.message.message_id,
        chat_id=callback.from_user.id,
        text=text,
        reply_markup=kb
    )
