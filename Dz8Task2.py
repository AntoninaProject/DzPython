#Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

import telebot
from pickle import load


def send_answers():
    with open("token.txt") as file:
        token = file.read()
    bot = telebot.TeleBot(token)

    try:
        with open("users_appeals.apls", "rb") as file:
            try:
                while True:
                    appeal = load(file)
                    print(appeal)
                    answer = f"Ответ на ваше обращение № {appeal.appeal_time}:\n\n\"{appeal.appeal_text}\"\n\n"
                    answer += input("Введите ответ пользователю:\n")
                    bot.send_message(appeal.user_id, answer)
            except EOFError:
                print("end")
    except FileNotFoundError:
        print("Обращений нет")


send_answers()