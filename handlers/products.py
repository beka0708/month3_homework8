from aiogram import types
from config import bot

kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("Куплю недвижимость")
)
kb.add(
    types.KeyboardButton("Продам недвижимость")
)
kb.add(
    types.KeyboardButton("Сниму квартиру")
)
kb.add(
    types.KeyboardButton("Сдаю квартиру")
)


async def show_products(call: types.CallbackQuery):
    # chat_id = message.from_user.id
    await call.message.answer(
        # chat_id=chat_id,
        text="welcome guest",
        reply_markup=kb
    )


async def threeroom(message: types.Message):
    await message.reply("Не найдено!")


async def address(call: types.CallbackQuery):
    await call.message.answer(f'Кыргызская Республика 720004\n'
                        f'г. Бишкек, ул. Асанбай 27/1\n'
                        f'Тел.: +996 (507) 22-33-22\n'
                        f'email: info@house.kg\n')
