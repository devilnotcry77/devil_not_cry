from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
TOKEN = "Token for you bot"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(command=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Добро пожаловать,{msg.from_user.first_name}')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Я не понимаю')

if __name__ == '__main__':
    executor.start_polling(dp)