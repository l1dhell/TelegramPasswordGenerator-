import secrets
import string
from aiogram import Bot, Dispatcher,executor,types
from config import TOKEN,ADMIN
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def GeneratePassword(pwd_length):
    pwd_length = int(pwd_length)
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

Keyboard = InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
Button_DoGenerate = InlineKeyboardButton("Generate Password",callback_data="Generate Password")
Button_SetValue = InlineKeyboardButton("Set password length",callback_data="Set your lenght")
Keyboard.add(Button_DoGenerate)
Keyboard.add(Button_SetValue)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.callback_query_handler(text=["Generate Password","Set your lenght"])
async def Generator(call:types.CallbackQuery):
    if call.data == "Generate Password":
        await call.message.answer(f"{GeneratePassword(12)}",reply_markup=Keyboard)
    if call.data == "Set your lenght":
        await call.message.answer("Send me a value")
        LenghtPassword = call.data
        await call.message.answer(f"{GeneratePassword(LenghtPassword)}")


#Включение бота
async def on_startup(_):
    await bot.send_message(ADMIN, "Bot is ready")
    print("Bot is working")

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("Hello",reply_markup=Keyboard)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
