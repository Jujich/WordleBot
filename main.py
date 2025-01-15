from aiogram import Dispatcher
from bot import bot
import asyncio
from game.start import start, restart
from game.stats import stats
from game.play import play, handle_guess
from game import handle_delete_message, rules

dp = Dispatcher()
dp.include_routers(
    start.router,
    restart.router,
    stats.router,
    play.router,
    handle_guess.router,
    handle_delete_message.router,
    rules.router,
)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Bot running...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("KeyboardInterrupt, shutting down...")
