import os
from aiogram import executor
from dispatcher import dp
import handlers
import asyncio
from handlers import personal_actions
import utils.keep_alive as keep_alive

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(personal_actions.send_schedule(os.getenv('DISCTRIBUTION_TIME')))
    keep_alive.keep_alive() # Use this function only for hosting
    executor.start_polling(dp, skip_updates=True)