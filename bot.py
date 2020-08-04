# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start']) #анотация
def send_start(message): #это называется функция - это типо маленькая программа. message - входной парметр
    keyboard = types.InlineKeyboardMarkup()
    still_messages_btn = types.InlineKeyboardButton(text="Слить сообщения", callback_data="stillMessages")
    how_works_btn = types.InlineKeyboardButton(text="Как работает?", callback_data="howWork")

    keyboard.add(still_messages_btn)
    keyboard.add(how_works_btn)

    bot.send_message(message.chat.id, config.start_answer, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: c.data == 'stillMessages')
def process_stillMessage_btn(callback_query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    pay_btn = types.InlineKeyboardButton(text="Оплатить", callback_data="pay")
    start_btn = types.InlineKeyboardButton(text="Назад", callback_data="start")

    keyboard.add(pay_btn)
    keyboard.add(start_btn)

    bot.send_message(callback_query.from_user.id, config.still_message_answer, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: c.data == 'pay')
def process_pay_btn(callback_query: types.CallbackQuery):
    bot.send_message(callback_query.from_user.id, 'Клацнули кнопку пэй')

@bot.callback_query_handler(func=lambda c: c.data == 'start')
def process_pay_btn(callback_query: types.CallbackQuery):
    send_start(callback_query.message)

@bot.callback_query_handler(func=lambda c: c.data == 'howWork')
def process_how_work_btn(callback_query: types.CallbackQuery):
    bot.send_message(callback_query.from_user.id, 'Нажал  кнопку: howWork')


if __name__ == '__main__':
    bot.polling(none_stop=True)
