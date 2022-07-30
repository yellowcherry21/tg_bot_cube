from _thread import start_new_thread
import locale
import utils
import telebot
from telebot import types
from telebot import TeleBot
locale.setlocale(locale.LC_ALL)

bot = telebot.TeleBot("5467360653:AAGyE0Uqq-zktKDirlcSdskUtdz09NJHxIc")
greeting = '''АЛЁ ЕБЛАНЫ ИГРА НАЧАЛАСЬ
ДЕЛАЕМ СТАВКИ
'''


@bot.message_handler(commands=["start"])
def start_func(message: types.Message):
    bot.send_message(message.chat.id, greeting)
    start_new_thread(utils.playing, (message,))


@bot.message_handler(commands=["reg"])
def register_user(message: types.Message):
    utils.save_user(message.from_user)
    bot.send_message(message.chat.id, "Зарегал тебя")


@bot.message_handler(commands=["cube"])
def throw_cube(message: types.Message):
    dice_value = bot.send_dice(chat_id=message.chat.id, emoji="🎲").dice.value


bot.infinity_polling()
