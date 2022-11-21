import random
from aiogram import Bot, Dispatcher,executor,types
from config import TOKEN,ADMIN
from keyboards import Keyboard,LenghtKeyboard
from GeneratorPassword import GeneratePassword

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(text=["Generate Password","Set your lenght","Link to password generator","Information about the Creator"])
async def Generator(call:types.CallbackQuery):
    if call.data == "Generate Password":
        await call.message.answer(f"{GeneratePassword(12)}",reply_markup=Keyboard)
        await call.message.delete()

    if call.data == "Set your lenght":
        await call.message.answer("Choose password length",reply_markup=LenghtKeyboard)
        await call.message.delete()

    if call.data == "Information about the Creator":
        await call.message.answer("https://telegra.ph/School-Project-11-21",reply_markup=Keyboard)
        await call.message.delete()

    if call.data == "Link to password generator":
        await call.message.answer("https://drive.google.com/file/d/1CKkAMvssWZWUYUoViJs-c5Qn-YeIMt-5/view?usp=share_link",reply_markup=Keyboard)
        await call.message.delete()


@dp.callback_query_handler(text=["0-8","9-12","13-16","17-20","21-24","25-30"])
async def SetLenght(call:types.CallbackQuery):

    if call.data == "0-8":
        Value = random.randint(0,8)
        await call.message.answer(f"{GeneratePassword(Value)}", reply_markup=Keyboard)
        await call.message.delete()

    if call.data == "9-12":
        Value = random.randint(9,12)
        await call.message.answer(f"{GeneratePassword(Value)}", reply_markup=Keyboard)
        await call.message.delete()

    if call.data == "13-16":
        Value = random.randint(13,16)
        await call.message.answer(f"{GeneratePassword(Value)}", reply_markup=Keyboard)
        await call.message.delete()

    if call.data == "17-20":
        Value = random.randint(17,20)
        await call.message.answer(f"{GeneratePassword(Value)}", reply_markup=Keyboard)
        await call.message.delete()

    if call.data == "21-24":
        Value = random.randint(21,24)
        await call.message.answer(f"{GeneratePassword(Value)}", reply_markup=Keyboard)
        await call.message.delete()

    if call.data == "25-30":
        Value = random.randint(25,30)
        await call.message.answer(f"{GeneratePassword(Value)}", reply_markup=Keyboard)
        await call.message.delete()


async def on_startup(_):
    await bot.send_message(ADMIN, "Bot is ready")
    print("Bot is working")

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("Hello",reply_markup=Keyboard)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
