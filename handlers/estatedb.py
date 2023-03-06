from aiogram import types
import db
from config import bot,dp
from db import base
from db.base import get_products
from handlers.user_info_fsm import start_user_dialog


async def grafik(message: types.Message):
    await message.reply("""
График работы: 
Понедельник - Пятница с 09:00 до 18:00 
Суббота с 10:00 до 17:00
Воскресенье - выходной
    
с 13:00 до 14:00 обеденный перерыв 
    """)


def kb_buy(product_id: int):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(
        text="Buy",
        callback_data=f'buy_product_{product_id}'))
    return kb
    # await message.answer("""
    # Каталог книг
    # """)


async def catalog(message: types.Message):
    products = [
        (1, 'The Witcher book 1', 500, 'images/witcher1.jpeg'),
        (2, 'The Witcher book 2', 600, 'images/witcher2.jpeg'),
        (3, 'The Witcher book 3', 700, 'images/witcher3.jpeg')]
    await message.answer(
        text="Наши товары:"
    )
    for product in products:
        # print(product)
        # with open(product[3], 'rb') as image:
        await message.answer_photo(
                    photo=open(product[3],'rb'),
                    caption=f'Товар: {product[1]}\n Цена:{product[2]}',
                    reply_markup=kb_buy(product[0])
            )

async def lot3(message: types.Message):
    await message.reply("""
    электронные книги, будут позже
""")