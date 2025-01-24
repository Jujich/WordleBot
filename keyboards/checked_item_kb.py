from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from strings.keyboard_strings import keyboard_strings_ru, keyboard_strings_en
from db.db_requests import get_user_settings, get_user_language


async def get_user_settings_kb(user_id: int) -> InlineKeyboardMarkup:
    user_language = await get_user_language(user_id)
    if user_language == "en":
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_en["language"], callback_data="language_info"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_en["language_en"], callback_data="language_en"),
            InlineKeyboardButton(text=keyboard_strings_en["language_ru"], callback_data="language_ru"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_en["tries"], callback_data="tries_info"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_ru["tries_1"], callback_data="tries_1"),
            InlineKeyboardButton(text=keyboard_strings_en["tries_6"], callback_data="tries_6"),
            InlineKeyboardButton(text=keyboard_strings_en["tries_10"], callback_data="tries_10"),
            InlineKeyboardButton(text=keyboard_strings_en["tries_20"], callback_data="tries_20"),
            InlineKeyboardButton(text=keyboard_strings_en["tries_inf"], callback_data="tries_inf"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_en["close"], callback_data="delete_message"),
        )
        keyboard = builder.as_markup()
    else:
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_ru["language"], callback_data="language_info"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_ru["language_en"], callback_data="language_en"),
            InlineKeyboardButton(text=keyboard_strings_ru["language_ru"], callback_data="language_ru"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_ru["tries"], callback_data="tries_info"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_ru["tries_1"], callback_data="tries_1"),
            InlineKeyboardButton(text=keyboard_strings_ru["tries_6"], callback_data="tries_6"),
            InlineKeyboardButton(text=keyboard_strings_ru["tries_10"], callback_data="tries_10"),
            InlineKeyboardButton(text=keyboard_strings_ru["tries_20"], callback_data="tries_20"),
            InlineKeyboardButton(text=keyboard_strings_ru["tries_inf"], callback_data="tries_inf"),
        )
        builder.row(
            InlineKeyboardButton(text=keyboard_strings_ru["close"], callback_data="delete_message"),
        )
        keyboard = builder.as_markup()

    data = await get_user_settings(user_id)
    for row in keyboard.inline_keyboard:
        for button in row:
            try:
                if button.callback_data.split("_")[1] == data[button.callback_data.split("_")[0]]:
                    button.text = button.text + " ✅"
                else:
                    button.text.replace(" ✅", "")
            except KeyError:
                continue

    return keyboard
