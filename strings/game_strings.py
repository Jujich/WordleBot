from string import Template

game_strings = {
    "rules": "Here are the rules of <b>Wordle</b>:\n\n"
             " — Unlike regular <b>Wordle</b> - you can guess as much words as you like per day.\n"
             " — The main goal of the game is to guess a 5-letter word in 6 tries.\n"
             " — After each guess, the color of the tiles below the word will change to show how close your guess was.\n"
             "   • 🟩 Green tile means that the letter is in the word and in the correct spot.\n"
             "   • 🟨 Yellow tile means that the letter is in the word but in the wrong spot.\n"
             "   • ⬜️ Grey tile means that the letter is not in the word.\n"
             " — See your stats to show your progress.\n\n"
             "<i>Have fun!</i>",
    "play_start": "Alright, lets play!\n"
                  "Guess the word, you have <b>6</b> tries!",
    "guess_wrong_length": "Your guess must be a 5-letter word!",
    "wrong_guess": Template(
        "<i>Tries left:</i> <b>$tries_left/6</b>\n\n"
        "$guess\n"
        "$tiles"
    ),
    "not_a_word": Template(
        "$guess is not a word!\n"
    ),
    "correct_guess": Template(
        "You guessed it! The word was <b>$word</b>.\n"
        "Use /stats to see your stats or /play to try again!"
    ),
    "out_of_tries": "You're out of tries!\n"
                    "Use /stats to see your stats or /play to try again!",
}
