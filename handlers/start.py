from aiogram import types

import commands
import texts
from loader import dp
import keyboards as kb


@dp.message_handler(commands=commands.START, state='*')
async def welcome(msg: types.Message):
    await msg.answer(texts.welcome)
    await msg.answer(texts.ask_amount, reply_markup=kb.AmountOptions())
