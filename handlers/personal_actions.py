import asyncio
from aiogram import types
from dispatcher import bot, dp, db, al
from datetime import datetime


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user({
            'user_id': message.from_user.id,
            'status': False
        })

    await message.answer('Welcome!')


@dp.message_handler(commands='subscribe')
async def subscribe(message: types.Message):
    if not db.get_subscriber(message.from_user.id):
        db.subscribe_user(message.from_user.id)
        await message.answer('✅ Вы успешно подписались на рассылку.')    
    else:
        await message.answer('❌ Вы уже подписаны на рассылку.')    


@dp.message_handler(commands='unsubscribe')
async def unsubscribe(message: types.Message):
    if db.get_subscriber(message.from_user.id):
        db.unsubscribe_user(message.from_user.id)
        await message.answer('✅ Вы успешно отписались от рассылки.')    
    else:
        await message.answer('❌ Вы уже отписаны от рассылки.')   


async def send_schedule(time: str):
    while True:
        if datetime.now().strftime('%H:%M:%S') == time:
            animes = al.get_anime_schedule()[datetime.today().weekday()]
            subs = db.get_subscribers()

            for sub in subs:
                await bot.send_message(
                    sub['user_id'], 
                    '<b>Сегодня по расписанию на <a href="{0}">AniLibria</a>:</b> \n\n' + ''
                    .format(al.url)
                    .join(
                        '• <a href="{0}">{1}</a>\n'.format(anime['link'], anime['name']) for anime in animes
                    )
                )

        await asyncio.sleep(1)    
