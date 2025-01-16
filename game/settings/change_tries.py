from aiogram import Router, F
from aiogram.types import CallbackQuery
from db.db_requests import get_user_settings, update_user_tries
from strings.menu_strings import menu_strings_en, menu_strings_ru
from keyboards.prebuilt import close_kb_en, close_kb_ru
from keyboards.checked_item_kb import get_user_settings_kb
from bot import bot

router = Router()


@router.callback_query(F.data.regexp(r"tries_\w{1,}"))
async def change_tries(callback: CallbackQuery):
    user_settings = await get_user_settings(callback.from_user.id)
    tries = callback.data[6:]
    if await update_user_tries(callback.from_user.id, tries):
        user_settings["tries"] = tries
    kb = await get_user_settings_kb(callback.from_user.id)
    text = menu_strings_en["settings"] if user_settings["language"] == "en" else menu_strings_ru["settings"]
    await bot.edit_message_text(
        message_id=callback.message.message_id,
        chat_id=callback.from_user.id,
        text=text,
        reply_markup=kb
    )
