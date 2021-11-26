from aiogram import types

import keyboards as kb
from loader import dp


@dp.callback_query_handler(button=kb.AmountOptions.OPTION, state='*')
async def _(query: types.CallbackQuery, button: dict):
    await query.answer('😔 Платежная система еще не подключена')
