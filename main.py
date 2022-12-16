import aiogram
from aiogram import Bot, Dispatcher
import os

import handlers.audio
import handlers.file
import handlers.finish
import handlers.text
import handlers.photo
import asyncio

# Run bot
async def main():
    bot = Bot(token=os.environ['TOKEN'], parse_mode="HTML")
    dp = Dispatcher()
    
    dp.include_router(handlers.finish.router)
    dp.include_router(handlers.audio.router)
    dp.include_router(handlers.photo.router)
    dp.include_router(handlers.file.router)
    dp.include_router(handlers.text.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
