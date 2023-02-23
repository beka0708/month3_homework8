from aiogram import Bot, Dispatcher
# from dotenv import load_dotenv
# from os import getenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from apscheduler.schedulers.asyncio import AsyncIOScheduler

# load_dotenv()
# bot = Bot(token=getenv('BOT_TOKEN'))

BOT_TOKEN = '6112163266:AAE_rDyiQ3evaVS-6vJdekIXwntLGyWjHAI'

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# scheduler = AsyncIOScheduler()

