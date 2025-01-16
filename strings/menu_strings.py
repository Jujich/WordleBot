from string import Template

menu_strings_en = {
    "start": "👋 Greetings! I'm a <b>Wordle</b> bot.\n\n"
             "🎮 Use /play to play a game of Wordle\n"
             "📕 Use /rules if you don't know how to play\n"
             "📊 Use /stats to see your stats\n"
             "⚙️ Use /settings to change your settings\n\n"
             "💬 See the commands list to discover what else I can do!",
    "start_logged": "<b><i>🔴 Hey!</i></b>\nYou're already logged in!",
    "restart": "🔄 Bot has been reloaded!",
    "stats": Template(
        "📊 Here are your stats:\n\n"
        "<b>Casual:</b>\n"
        "🎮 Games played: <b>$games</b>\n"
        "✅ Guessed correct: <b>$win</b>\n"
        "❌ Guessed wrong: <b>$lose</b>\n"
        "➗ Guess rate: <b>$guess_rate</b>\n\n"
        "<b>Dailies:</b>\n"
        "🎮 Dailies played: <b>$dailies</b>\n"
        "✅ Guessed correct: <b>$dwin</b>\n"
        "❌ Guessed wrong: <b>$dlose</b>\n"
        "📈 Daily streak: <b>$streak</b>\n"
        "🔥 Longest daily streak: <b>$longest_streak</b>"
    ),
    "settings": "⚙️ You can change your settings here!",
    "info_error": "❌ Something went wrong, please use /restart to restart the bot",
    "language_info": "🌐 You can change your language with the buttons below",
    "tries_info": "🔢 You can change your amount of tries with the buttons below",
}

menu_strings_ru = {
    "start": "👋 Привет! Я бот для игры в <b>Wordle</b>.\n\n"
             "🎮 Используйте /play чтобы сыграть в <b>Wordle</b>\n"
             "📕 Используйте /rules если не знаете правил игры\n"
             "📊 Используйте /stats чтобы посмотреть свою статистику\n"
             "⚙️ Используйте /settings чтобы открыть настройки\n\n"
             "💬 Посмотрите список команд, чтобы узнать, что ещё я могу!",
    "start_logged": "<b><i>🔴 Эй!</i></b>\nВы уже вошли!",
    "restart": "🔄 Бот был перезагружен!",
    "stats": Template(
        "📊 Вот ваша статистика:\n\n"
        "<b>Обычный:</b>\n"
        "🎮 Сыграно игр: <b>$games</b>\n"
        "✅ Угадано правильно: <b>$win</b>\n"
        "❌ Угадано неправильно: <b>$lose</b>\n"
        "➗ % правильных: <b>$guess_rate</b>\n\n"
        "<b>Ежедневный:</b>\n"
        "🎮 Ежедневных попыток: <b>$dailies</b>\n"
        "✅ Правильно: <b>$dwin</b>\n"
        "❌ Неправильно: <b>$dlose</b>\n"
        "📈 Ежедневный стрик: <b>$streak</b>\n"
        "🔥 Макс. ежедневный стрик: <b>$longest_streak</b>"
    ),
    "settings": "⚙️ Здесь вы можете поменять настройки игры!",
    "info_error": "❌ Что-то пошло не так, используйте /restart чтобы перезапустить бота",
    "language_info": "🌐 С помощью кнопок ниже вы можете поменять свой язык",
    "tries_info": "🔢 С помощью кнопок ниже вы можете поменять кол-во попыток",
}
