from string import Template

game_strings_en = {
    "rules": "ℹ️ Here are the rules of <b>Wordle</b>:\n\n"
             "1️⃣ The main goal of the game is to guess a 5-letter word.\n"
             "2️⃣ After each guess, the color of the tiles below the word will change to show how close your guess was.\n"
             "   • 🟩 Green tile means that the letter is in the word and in the correct spot.\n"
             "   • 🟨 Yellow tile means that the letter is in the word but in the wrong spot.\n"
             "   • ⬜️ Grey tile means that the letter is not in the word.\n"
             "3️⃣ You can use /stats to see your stats.\n\n"
             "<i>Have fun!</i>",
    "play_start": Template(
        "👌 Alright, lets play!\n"
        "❓ Guess the word, you have <b>$tries</b> tries!"
    ),
    "play_daily": "👌 Alright, lets play daily mode!\n"
                  "❓ Guess the word, you have <b>6</b> tries!\n",
    "daily_completed": "❌ You've already played the daily mode today! Try again tomorrow!",
    "guess_wrong_length": "Your guess must be a 5-letter word!",
    "game_already_started": "❌ You have already started a game!",
    "wrong_guess": Template(
        "<i>Tries left:</i> <b>$tries_left/$tries</b>\n\n"
        "$guess\n"
        "$tiles"
    ),
    "not_a_word": Template(
        "$guess is not a word!\n"
    ),
    "correct_guess": Template(
        "🏆 You guessed it!\n\n"
        "The word was: <b>$word</b>.\n\n"
        "Use /stats to see your stats or /play to try again!"
    ),
    "out_of_tries": Template(
        "❌ You're out of tries!\n\n"
        "The word was: <b>$word</b>\n\n"
        "Use /stats to see your stats or /play to try again!"
    ),
    "game_stopped": "❌ The game has been stopped.",
}

game_strings_ru = {
    "rules": "ℹ️ Вот правила игры <b>Wordle</b>:\n\n"
             "1️⃣ Цель игры - угадать слово из 5 букв.\n"
             "2️⃣ После каждой попытки цвет каждой из иконок под буквой будет меняться в зависимости от того, насколько близка была Ваша догадка.\n"
             "   • 🟩 Зеленый значит что буква есть в слове и находится в правильной позиции.\n"
             "   • 🟨 Желтый значит что буква есть в слове, но находится на неправильной позиции.\n"
             "   • ⬜️ Серый значит что буквы нет в слове.\n"
             "3️⃣ Вы можете использовать /stats для просмотра своей статистики.\n\n"
             "<i>Удачи!</i>",
    "play_start": Template(
        "👌 Итак, давайте сыграем!\n"
        "❓ Угадайте слово, у вас есть <b>$tries</b> попыток!"
    ),
    "play_daily": "👌 Итак, давайте угадывать ежедневное слово!\n"
                  "❓ У Вас есть <b>6</b> попыток!\n",
    "daily_completed": "❌ Вы уже отгадывали ежедневное слово сегодня! Возвращайтесь завтра!",
    "guess_wrong_length": "Слово должно быть из 5 букв!",
    "game_already_started": "❌ Вы уже начали игру!",
    "wrong_guess": Template(
        "<i>Осталось попыток:</i> <b>$tries_left/$tries</b>\n\n"
        "$guess\n"
        "$tiles"
    ),
    "not_a_word": Template(
        "$guess не является словом!\n"
    ),
    "correct_guess": Template(
        "🏆 Правильно!\n\n"
        "Слово было:<b>$word</b>.\n\n"
        "Используйте /stats для просмотра статистики или /play чтобы сыграть ещё!"
    ),
    "out_of_tries": Template(
        "❌ Попыток больше нет!\n\n"
        "Слово было: <b>$word</b>\n\n"
        "Используйте /stats для просмотра статистики или /play чтобы сыграть ещё!"
    ),
    "game_stopped": "❌ Игра остановлена.",
}
