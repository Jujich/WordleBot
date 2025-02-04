from string import Template

error_strings_en = {
    "unknown_command": Template("❌ Unknown command: $command"),
    "user_not_exist": "💤 It seems like you haven't played yet!\n"
                      "▶️ Use /start to get started!",
    "daily_not_exist": "❌ There's some problem with the daily, please try again later",
    "error_leaderboard": "❌ There's some problem with the leaderboard, please try again later",
}

error_strings_ru = {
    "unknown_command": Template("❌ Неизвестная команда: $command"),
    "user_not_exist": "💤 Похоже вы тут в первый раз!\n"
                      "▶️ Используйте /start чтобы начать играть!",
    "daily_not_exist": "❌ С ежедневным испытанием возникла проблема, пожалуйста, попробуйте позже",
    "error_leaderboard": "❌ С таблицей лидеров возникла проблема, пожалуйста, попробуйте позже",
}
