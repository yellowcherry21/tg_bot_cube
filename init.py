from telebot import TeleBot
import psycopg2 as pg

GAME_OVER = "GAME OVER"
QUERIES = {"set_flag": '''UPDATE public."Availability" 
            SET flag = %s 
            WHERE id = %s''',
           "get_flag_by_id": """SELECT flag FROM public."Availability" WHERE id = %s"""
           }
GREETING = '''АЛЁ ЕБЛАНЫ ИГРА НАЧАЛАСЬ
ДЕЛАЕМ СТАВКИ
'''
CHOOSE_NUMBER = "ВЫБИРАЙ БЛЯ ЦИФРУ ЕБЛАН"
CUBE_RESULT_ALERT = "ВЫПАЛО"
IS_PREDICTION_GOING = True

#bot_token = os.environ.get('BOT_TOKEN', None)
#bot_token = os.environ.get('BOT_TOKEN', None)


def init_bot():
    with open("bot_token.txt", "r") as bot_token_file:
        bot_token = bot_token_file.read()
    return TeleBot(bot_token)


def get_db_connection():
    return pg.connect(dbname='learn_db', user='postgres',
                      password='admin', host='localhost')
