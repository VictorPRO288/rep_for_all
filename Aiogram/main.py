from aiogram import Bot, Dispatcher
from utils.Tokenizer import Tokenizer
import asyncio
from os import getenv
from dotenv import load_dotenv
from handlers.router import router


load_dotenv()
TG_TOKEN = getenv("TG_TOKEN")


dp = Dispatcher()

dp.include_router(router)


async def main():
    bot = Bot(token=TG_TOKEN)
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())
