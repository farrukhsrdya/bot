import sqlite3



connection = sqlite3.connect('delivery.db', check_same_thread=False)

sql = connection.cursor()



sql.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, number TEXT UNIQUE, location TEXT);')




def register(tg_id, name, num, location):
    sql.execute('INSERT INTO users VALUES (?, ?, ?, ?);', (tg_id, name, num, location))

    connection.commit()

def check_user(tg_id):
    a = sql.execute('SELECT * FROM users WHERE id=?;', (tg_id,)).fetchone()
    if a:
        return a
    else:
        return False








