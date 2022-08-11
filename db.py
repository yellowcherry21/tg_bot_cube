import psycopg2 as pg

QUERIES = {"set_flag": '''UPDATE public."Availability" 
            SET flag = %s 
            WHERE id = %s''',
           }


con = pg.connect(dbname='learn_db', user='postgres',
                        password='admin', host='localhost')

def set_flag(chat_id, flag):
    with con, con.cursor() as cursor:
            cursor.execute(QUERIES['set_flag'], (flag, chat_id))
    con.close()