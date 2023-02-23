# from aiogram import types
# from config import scheduler, bot
#
#
# async def notify_command_handler(message: types.Message):
#     scheduler.add_job(notify, 'interval', seconds=5, args=(message.from_user.id,)) # tuple with one element
#     await message.answer("Принято!")
#
# async def notify(user_id: int):
#     bot.send_message(
#         text = "Напоминалка!",
#         chat_id=user_id
#     )
#
# def get_products(message):
#     for ret in cur.execute("""SELECT * from products""").fetchall():
#
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\n цена: {ret[-1]}')