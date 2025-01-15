from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command
from db.db_requests import get_user_stats, check_user_exists
from bot import bot
from strings.menu_strings import menu_strings
from strings.errors import error_strings
from keyboards.prebuilt import close_kb

router = Router()


@router.message(Command("stats"))
async def stats(message: Message):
    await message.delete()
    if await check_user_exists(message.from_user.id):
        stats_ = await get_user_stats(message.from_user.id)
        streak = stats_["streak"]
        streak_str = str(streak)
        if streak >= 5:
            streak_str += "🔥"
        if streak >= 10:
            streak_str += "🔥"
        if streak >= 15:
            streak_str += "🔥"
        games = stats_["win"] + stats_["lose"]
        guess_rate = "0%"
        if games != 0:
            guess_rate = str(round(stats_["win"] / games * 100, 2)) + "%"
        await bot.send_message(
            chat_id=message.chat.id,
            text=menu_strings["stats"].substitute(
                games=games,
                win=stats_["win"],
                lose=stats_["lose"],
                guess_rate=guess_rate,
                streak=streak_str,
                longest_streak=stats_["longest_streak"],
            ),
            reply_markup=close_kb
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=error_strings["user_not_exist"],
            reply_markup=close_kb
        )
