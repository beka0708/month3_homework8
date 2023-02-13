
from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.start import (start, help, myinfo, gallery)
from handlers.products import (show_products, threeroom, address)
from handlers.estatedb import (lot1,lot2,lot3)

if __name__=="__main__":
    print(__name__)
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(gallery, commands=["gallery"])
    # dp.register_message_handler(show_products, commands=["products"])
    dp.register_callback_query_handler(show_products, Text(equals="products"))
    dp.register_message_handler(threeroom, Text(startswith="Продам недвижимость"))
    # dp.register_message_handler(address, Text(startswith="адрес"))
    dp.register_callback_query_handler(address, Text(equals='address'))
    dp.register_message_handler(lot1, Text(startswith="Куплю недвижимость"))
    dp.register_message_handler(lot2, Text(startswith="Сниму квартиру"))
    dp.register_message_handler(lot3, Text(startswith="Сдаю квартир"))
    executor.start_polling(dp)