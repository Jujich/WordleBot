from aiogram import Dispatcher
from bot import bot
import asyncio
from game.start import start, restart
from game.stats import stats
from game.play import play, handle_guess
from game import handle_delete_message, rules
from game.settings import (settings,
                           handle_info,
                           change_tries,
                           change_language)
from game.daily import daily
from game.daily.get_new_daily_word import run_daily_cycle


dp = Dispatcher()
dp.include_routers(
    start.router,
    restart.router,
    stats.router,
    play.router,
    handle_guess.router,
    handle_delete_message.router,
    rules.router,
    settings.router,
    handle_info.router,
    change_language.router,
    change_tries.router,
    daily.router,
)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(
        dp.start_polling(bot),
        run_daily_cycle()
    )


if __name__ == "__main__":
    try:
        print("Bot running...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("KeyboardInterrupt, shutting down...")
