import sqlite3
from pathlib import Path

from aiogram.types import message
from config import bot
import random


def db_init():
    DB_PATH = Path(__file__).parent.parent
    DB_FILE = 'db.sqlite'
    global db, cur  # orm
    db = sqlite3.connect(DB_PATH / DB_FILE)
    cur = db.cursor()
    print(DB_PATH)


def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    name TEXT ,
    price REAL,
    photo TEXT
    ) """)

    cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER 
    user_name TEXT,
    address TEXT,
    product_id INTEGER,
    PRIMARY KEY (order_id),
    FOREIGN KEY (product_id) REFERENCES products(products_id)
    ON DELETE CASCADE
    )""")

    db.commit()


def delete_tables():
    cur.execute("""DROP TABLE IF EXISTS products""")
    db.commit()


def populate_products():
    cur.execute("""INSERT INTO products (name, price, photo) VALUES
                            ('The Witcher book 1', 500, 'images/witcher1.jpeg'),
                            ('The Witcher book 2', 600, 'images/witcher2.jpeg'),
                            ('The Witcher book 3', 700, 'images/witcher3.jpeg') 
                            """)
    db.commit()


def get_products():
    cur.execute("""SELECT * from products""")
    all_products = cur.fetchall()
    print(all_products)
    return all_products

    # name, price, photo = random.choice(all_products)
    # text = f'{name} {price} {photo} Caption: Books'
    # bot.send_message(message.from_user.id, text)

    # return text

# def get_products(message):
#     for ret in cur.execute("""SELECT * from products""").fetchall():
#
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n цена: {ret[-1]}')

# def get_products():
# cur.execute("SELECT * FROM products")
# bookcat = cur.fetchall()
#
# for x in bookcat:
#     print(x)
#
# for ret in cur.execute("""SELECT * from products""").fetchall():
#     await bot.send_message()


if __name__ == "__main__":
    print(__name__)
    db_init()
    delete_tables()
    create_tables()
    populate_products()
    get_products()
