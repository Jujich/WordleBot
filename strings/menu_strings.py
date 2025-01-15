from string import Template

menu_strings = {
    "start": "Greetings! I'm a <b>Wordle</b> bot.\n\n"
             " - Use /play to play a game of Wordle\n"
             " - Use /stats to see your stats\n\n"
             "See the commands list to discover what else I can do!",
    "start_logged": "<b><i>Hey!</i></b>\nYou're already logged in!",
    "restart": "Bot has been reloaded!",
    "stats": Template(
        "Here are your stats:\n\n"
        "Games played: <b>$games</b>\n"
        "Guessed correct: <b>$win</b>\n"
        "Guessed wrong: <b>$lose</b>\n"
        "Guess rate: <b>$guess_rate</b>\n"
        "Current streak: <b>$streak</b>\n"
        "Longest streak: <b>$longest_streak</b>"
    ),
}
