import asyncio
from aiogram import Bot, Dispatcher
from app.extensions import router
from app.config import BOT_API


# Polling, т.е бесконечный цикл проверки апдейтов
async def main():
    bot = Bot(token=BOT_API)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


# Функция main() запускается только в случае если скрипт запущен с этого файла
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')