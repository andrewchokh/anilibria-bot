import logging
from aiogram import Bot, Dispatcher
from classes.mongodb import MongoDB
from classes.anilibria import Anilibria
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)
db = MongoDB(os.getenv('MONGO_URI'))
al = Anilibria(os.getenv('ANILIBRIA_URL'))
