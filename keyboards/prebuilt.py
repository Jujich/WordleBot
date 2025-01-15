from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from strings.keyboard_strings import keyboard_strings

builder = InlineKeyboardBuilder()
builder.row(
    InlineKeyboardButton(text=keyboard_strings["close"], callback_data="delete_message"),
)
close_kb = builder.as_markup()
