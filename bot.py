import telebot
import log_generate as lg
from config import TOKEN_API
from telebot import types
import model as mr

bot = telebot.TeleBot(TOKEN_API)
chat_id = ''
message_id = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я бот калькулятор, если хочешь посчитать, вводи коммануду /calc")


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    lg.write_data(f'Бот получил команду "{message.text}"')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHhyhj2Q3G8_LnmlZTrKD5asKpoCTTjQACGCMAAu0HgUrqmupuzpQQ6y0E',
                     reply_markup=keyboard_start)


@bot.message_handler(commands=['calc'])
def calc_command(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHjotj23njbDoc0hH6f0DMmeghAQIGhwACXAADYIltDAgZgYxjUpb6LgQ')
    bot.send_message(message.chat.id, 'Вводи пример!')
    bot.register_next_step_handler(message, count_example)


def count_example(message):  # Функиця решения примера
    example, example_list = mr.get_nums(message.text)
    lg.write_data(f'Пользователь ввел пример: {example}')
    result = mr.get_result(example_list)
    lg.write_data(f'Получен ответ: {result}')
    bot.send_message(chat_id, f'{example} = {result}')


def start_bot():
    print('Server start!')
    bot.polling(none_stop=True)
