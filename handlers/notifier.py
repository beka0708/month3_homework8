from aiogram import types
from config import scheduler, bot

async def notify_command_handler(message: types.Message):
    scheduler.add_job(notify, 'interval', seconds=1, args=(message.from_user.id,)) # tuple with one element
    await message.answer("Принято!")

async def notify(user_id: int, message: types.Message):
    await message.answer("Введите напоминалку:")
    await bot.send_message(
        text="in_message",
        chat_id=user_id
    )
