from loader import dp
from .plug import Plug


def setup():
    dp.setup_middleware(Plug())
