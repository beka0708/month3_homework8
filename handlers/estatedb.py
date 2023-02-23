from aiogram import types
import db
from config import bot,dp
from db import base
from db.base import get_products
async def grafik(message: types.Message):
    await message.reply("""
График работы: 
Понедельник - Пятница с 09:00 до 18:00 
Суббота с 10:00 до 17:00
Воскресенье - выходной
    
с 13:00 до 14:00 обеденный перерыв 
    """)

async def catalog(message: types.Message):
    aa = get_products()
    # await message.reply("""
    # Каталог книг
    # """)
    await message.answer(text=aa )



async def lot3(message: types.Message):
    await message.reply("""
    электронные книги
""")