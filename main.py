import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.markdown import hbold

TOKEN = 'тут написать токен'

dp = Dispatcher()

#await message.answer(f"Hello, {hbold(message.from_user.full_name)}! \nГлавное меню")
#await message.answer(f'/info')

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
            [KeyboardButton(text='кнопка 1'), KeyboardButton(text='кнопка 2'), KeyboardButton(text='кнопка 3')], 
            [KeyboardButton(text='кнопка 5')]
        ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выбери кнопку", reply_markup=keyboard)

@dp.message(Command("инфа"))
async def cmd_info(message: types.Message):
    await message.answer("Этот бот умеет говорить какая погода, напиши название города")


@dp.message()
async def echo_handler(message: types.Message):
    if message.text == 'кнопка 2':
        kb = [
            [KeyboardButton(text='Купить'), KeyboardButton(text='Продать'), KeyboardButton(text='Баланс')], 
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Выбери кнопку", reply_markup=keyboard)
    elif message.text == 'кнопка 1':
        photo = open('logo.jpg', 'rb')
        await message.answer_photo(photo, caption="photo")
    else:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())