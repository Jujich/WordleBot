from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from strings.menu_strings import menu_strings_en, menu_strings_ru
from strings.errors import error_strings_en, error_strings_ru
from db.db_requests import get_user_language, get_leaderboard
from keyboards.prebuilt import close_kb_en, close_kb_ru

router = Router()


@router.message(Command("leaderboard"))
async def leaderboard(message: Message):
    await message.delete()
    lang = await get_user_language(message.from_user.id)
    strings = menu_strings_en if lang == "en" else menu_strings_ru
    err_strings = error_strings_en if lang == "en" else error_strings_ru
    kb = close_kb_en if lang == "en" else close_kb_ru
    leaderboard_data = await get_leaderboard()
    if leaderboard_data is not None:
        await message.answer(
            text=strings["leaderboard"].substitute(
                games=leaderboard_data["games"],
                guess_rate=leaderboard_data["guess_rate"],
                longest_streak=leaderboard_data["longest_streak"],
            ),
            reply_markup=kb
        )
    else:
        await message.answer(
            text=err_strings["error_leaderboard"],
            reply_markup=kb
        )
