#Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
from pickle import dumps
from appeal import Appeal


def run_tg_bot():
    info_text = "Я бот для сбора обращений.\nНапиши мне, а я передам твоё обращение в службу поддержки.\nFor help, type command \"/help\""
    commands_dict = {"/start": "starts bot",
                     "/help": "show help and available commands"}

    help_message = "Available commands:\n"
    for key in commands_dict:
        help_message += f"{key}: {commands_dict[key]}\n"
    help_message += info_text

    with open("token.txt") as file:
        token = file.read()
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, f"Привет {message.from_user.first_name}. {info_text}")

    @bot.message_handler(commands=["help"])
    def show_help(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, help_message)

    @bot.message_handler(content_types=["text"])
    def write_message_for_support(message):
        appeal_time = message.date
        appeal_text = message.text
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        appeal = Appeal(appeal_time=appeal_time,
                        user_id=user_id,
                        first_name=first_name,
                        last_name=last_name,
                        appeal_text=appeal_text)
        appeal = dumps(appeal)
        users_appeals.write(appeal)
        users_appeals.flush()
        bot.reply_to(message, f"Ваше обращение зарегистрировано под номером {appeal_time}.")

    bot.polling()


with open("users_appeals.apls", 'ab') as users_appeals:
    run_tg_bot()