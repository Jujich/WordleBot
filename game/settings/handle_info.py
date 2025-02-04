from aiogram.types import CallbackQuery
from aiogram import Router, F
from strings.menu_strings import menu_strings_en, menu_strings_ru
from db.db_requests import get_user_language

router = Router()


@router.callback_query(F.data.regexp(r"\w{1,}_info"))
async def handle_info(callback: CallbackQuery):
    lang = await get_user_language(callback.from_user.id)
    strings = menu_strings_en if lang == "en" else menu_strings_ru
    try:
        await callback.answer(
            show_alert=True,
            text=strings[callback.data]
        )
    except KeyError:
        await callback.answer(
            show_alert=True,
            text=strings["error"]
        )
