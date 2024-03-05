from aiogram import Bot, Dispatcher, executor
from handler import start_pip
from aiogram.contrib.fsm_storage.memory import MemoryStorage
API_TOKEN = '7033451663:AAEhLl2qc5pU7feUuqPfP2x_jO3PwU0fKco'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

start_pip(dp)


executor.start_polling(dp, skip_updates=True)
