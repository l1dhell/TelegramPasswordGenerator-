from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton

Keyboard = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True,one_time_keyboard=True)
Button_DoGenerate = KeyboardButton("/GeneratePassword")
Keyboard.row(Button_DoGenerate)
