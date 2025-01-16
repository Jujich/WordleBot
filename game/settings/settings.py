from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from strings.menu_strings import menu_strings_en, menu_strings_ru
from strings.errors import error_strings_en, error_strings_ru
from keyboards.prebuilt import close_kb_en, close_kb_ru
from keyboards.checked_item_kb import get_user_settings_kb
from db.db_requests import check_user_exists, get_user_language
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("settings"))
async def settings(message: Message, state: FSMContext):
    await message.delete()
    lang = await get_user_language(message.from_user.id)
    strings = menu_strings_en if lang == "en" else menu_strings_ru
    state_ = await state.get_state()
    state_data = await state.get_data()
    if state_ == "playing":
        guesses = state_data["guesses"]
        msg = await message.answer(
            text=strings["game_already_started"],
        )
        guesses.append(msg.message_id)
        await state.update_data(guesses=guesses)
        return
    error_strings = error_strings_en if lang == "en" else error_strings_ru
    clkb = close_kb_en if lang == "en" else close_kb_ru
    if not await check_user_exists(message.from_user.id):
        await message.answer(
            text=error_strings["user_not_exist"],
            reply_markup=clkb
        )
        return
    kb = await get_user_settings_kb(message.from_user.id)
    await message.answer(
        text=strings["settings"],
        reply_markup=kb
    )
