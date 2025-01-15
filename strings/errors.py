from string import Template

error_strings = {
    "unknown_command": Template("Unknown command: $command"),
    "user_not_exist": "It seems like you haven't played yet!\n"
                      "Use /start to get started!",
}
