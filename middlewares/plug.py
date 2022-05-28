from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

import config


class Plug(BaseMiddleware):

    @staticmethod
    async def on_pre_process_message(msg: types.Message, *_):
        if config.Bot.plug:
            await msg.answer('Настраиваем платежную систему...')
            raise CancelHandler
