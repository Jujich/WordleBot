from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from strings.keyboard_strings import keyboard_strings_en, keyboard_strings_ru

builder = InlineKeyboardBuilder()
builder.row(
    InlineKeyboardButton(text=keyboard_strings_en["close"], callback_data="delete_message"),
)
close_kb_en = builder.as_markup()
builder = InlineKeyboardBuilder()
builder.row(
    InlineKeyboardButton(text=keyboard_strings_ru["close"], callback_data="delete_message"),
)
close_kb_ru = builder.as_markup()
