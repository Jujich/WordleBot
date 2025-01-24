from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from strings.keyboard_strings import keyboard_strings_en, keyboard_strings_ru
import os

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


builder = InlineKeyboardBuilder()
builder.row(
    InlineKeyboardButton(text=keyboard_strings_en["edit_perms"], url=f"https://t.me/{os.environ.get('WORDLEBOT_USERNAME')}?startgroup=newgroups&admin=manage_chat+change_info+delete_messages+restrict_members+invite_users+promote_members"),
)
perms_kb_en = builder.as_markup()
builder = InlineKeyboardBuilder()
builder.row(
    InlineKeyboardButton(text=keyboard_strings_ru["edit_perms"], url=f"https://t.me/{os.environ.get('WORDLEBOT_USERNAME')}?startgroup=newgroups&admin=manage_chat+change_info+delete_messages+restrict_members+invite_users+promote_members"),
)
perms_kb_ru = builder.as_markup()
