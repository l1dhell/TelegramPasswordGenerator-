import secrets
import string
from aiogram import Bot, Dispatcher,executor,types
from config import TOKEN,ADMIN
from keyboards import Keyboard

def GeneratePassword(pwd_length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    #pwd_length = 12

    while True:
      pwd = ''
      for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

      if (any(char in special_chars for char in pwd) and
          sum(char in digits for char in pwd)>=2):
              break
    return pwd

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("Hello",reply_markup=Keyboard)

@dp.message_handler(commands=["GeneratePassword"],state=None)
async def Generator(message:types.message):
    await message.answer("Your password")
    Password = GeneratePassword(12)
    await message.answer(f":{Password}")

#Включение бота
async def on_startup(_):
    await bot.send_message(ADMIN, "Bot is ready")
    print("Bot is working")

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
