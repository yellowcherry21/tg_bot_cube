import os
from sqlite3 import DatabaseError
from telebot import types, TeleBot
import time


#with open("bot_token.txt", "r") as bot_token_file:
#   bot_token = bot_token_file.read()

bot_token = os.environ.get('BOT_TOKEN', None)

bot = TeleBot(bot_token)


def playing(message: types.Message):
    prediction_locker(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    btn5 = types.KeyboardButton("5")
    btn6 = types.KeyboardButton("6")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(
        message.chat.id, text="ВЫБИРАЙ БЛЯ ЦИФРУ ЕБЛАН", reply_markup=markup)

    time.sleep(30)
    
    database_set_flag(message.chat.id, False)

    result = throw_cube(message)
    bot.send_message(message.chat.id, f"ВЫПАЛО {result}")


def save_user(user: types.User):
    with open("users.txt", "a", encoding="UTF-8") as users_file:
        users_file.write(str(user.id) + "," +
                         str(user.first_name)+"," +
                         str(user.username)+",0\n")


def throw_cube(message: types.Message) -> int:
    return bot.send_dice(chat_id=message.chat.id, emoji="🎲").dice.value


def save_prediction(message: types.Message):
    with open("user_predictions.txt", "r+t", encoding="UTF-8") as user_predictions:
        id = int(user_predictions.readlines()[-1].split(",")[0]) + 1
        user_predictions.write(str(id) + "," +
                               str(message.from_user.id) + "," +
                               str(message.date) + "," +
                               str(message.text)+"\n")

def prediction_locker(id: int):
    flag = get_flag(id)
    if not flag:
        database_set_flag(id, True)
