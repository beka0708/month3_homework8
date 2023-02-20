from aiogram import types
import random

kb = types.InlineKeyboardMarkup()
kb.add(types.InlineKeyboardButton(
    text="Наши услуги:",
    callback_data="products"
))
kb.add(types.InlineKeyboardButton(
    text="Наш адрес:",
    callback_data="address"
))

# @dp.message_handler(commands=["start"])
async def start(message:types.Message):
    user = message.from_user.full_name
    await message.answer(
        f'Приветствуем, {user}!\n Добро пожаловать в агентство недвижимости <<House.kg>>!')
    await message.reply(
        f'Выберите команду:',
        reply_markup=kb
    )
# @dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        """
        /start 
/help - Список команд:
/myinfo - Данные пользователя
/gallery - random photos
/products - Наши услуги
        """
    )
# @dp.message_handler(commands=["myinfo"])
async def myinfo(message: types.Message):
    user = message.from_user.full_name
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    await message.answer(
        f'Username: {user}\n'
        f'User ID: {user_id}\n'
        f'User first name: {first_name}\n'
        f'User last name: {last_name}\n'
    )
    # await message.delete()
# @dp.message_handler(commands=["picture"])
async def gallery(message: types.Message):
    photos = ['images/house1.jpeg','images/house2.jpeg','images/house3.jpeg','images/house4.jpeg']
    with open(random.choice(photos), 'rb') as photos:
        await message.answer_photo(
            photo = photos,
            caption = 'houses'
        )
