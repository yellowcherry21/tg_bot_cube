from _thread import start_new_thread
import locale
import utils
from telebot import types
from telebot import TeleBot
locale.setlocale(locale.LC_ALL)

with open("bot_token.txt","r") as bot_token_file:
    bot_token = bot_token_file.read()

bot = TeleBot(bot_token)
greeting = '''АЛЁ ЕБЛАНЫ ИГРА НАЧАЛАСЬ
ДЕЛАЕМ СТАВКИ
'''


@bot.message_handler(commands=["startt"])
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
