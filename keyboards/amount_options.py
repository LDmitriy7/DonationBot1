from aiogram.types import InlineKeyboardMarkup
from aiogram_utils.keyboards import InlineKeyboardButton


class AmountOptions(InlineKeyboardMarkup):
    OPTION = InlineKeyboardButton('{amount} RUB', callback_data='amount_options:{amount}')

    def __init__(self):
        super().__init__(row_width=1)

        for a in [79, 149, 299, 499]:
            self.add(
                self.OPTION.format(amount=a)
            )
