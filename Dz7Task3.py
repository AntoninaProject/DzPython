#Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.

import random
import telebot
from telebot import types

game_started = False
r_number = 0

token = '6043570265:AAFJ5q7QB4or1vHYo6wxvoagme1n_n0qcuI'
bot = telebot.Telebot(token)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn3 = types.KeyboardButton('играть')
markup.add(itembtn3)


@bot.message_handler(commands=['start', 'help'])
def send_welkome(message):
    bot.send_message(massage.from_user.id, "Хочешь поиграть? Напиши '/играть'", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def read_text_commands(message):
    global game_started
    global r_number

if game_started:
    if message.text.isdigit():
        number = int(message, text)
        if number > r_number:
            bot.reply_to(message, 'Меньше')
        elif number < r_number:
            bot.reply_to(message, 'Больше'!)
        elif number = r_number:
            game_started = False
            bot.reply_to(message, f'Молодец! Ты угадал! Я загадал число {r_number}!')
        else:
            bot.reply_to(message, 'Ничего не понял... Попробуй ещё раз.')
        else:
           bot.reply_to(message, 'Я ожидал число...')

    elif message.text == 'играть':
         if not game_started:
            game_started = True
            r_number = random.randint(1, 1000)
            bot.reply_to(message, 'Я задумал число от 1 до 1000! Попробуй его отгадать!')
        else 
           bot.reply_to(message, 'Игра уже идёт! Отгадай число!')
    elif message.text == 'вычислить':
        bot.reply_to(message, 'Введи выражение!')
        bot.register_next_step_handler(message, calculate)

def calculate(message):
    try:
        bot.reply_to(message, f'Ответ: {eval(message.text)}')
    except NameError:
        bot.reply_to(message, f'Вы ввели неверное выражение')




bot.infinity_polling()



       
                         
        
