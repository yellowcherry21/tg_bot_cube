from init import init_bot, GREETING, CHOOSE_NUMBER, CUBE_RESULT_ALERT, GAME_OVER
from telebot import types
import time
import db


bot = init_bot()


def playing(message: types.Message):
    chat_id = message.chat.id
    if not is_playing(chat_id):
        db.set_flag(chat_id, True)
        init_game(chat_id)

        time.sleep(30)

        result = throw_cube(message)
        bot.send_message(chat_id, f"{CUBE_RESULT_ALERT} {result}")
    db.set_flag(chat_id, False)
    bot.send_message(chat_id, GAME_OVER)


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


def is_playing(id: int):
    return db.get_flag_by_id(id)


def init_game(chat_id):
    bot.send_message(chat_id, GREETING)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    btn5 = types.KeyboardButton("5")
    btn6 = types.KeyboardButton("6")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(chat_id, text=CHOOSE_NUMBER, reply_markup=markup)


def reg_chat(id:int)->None:
    db.save_chat(id)