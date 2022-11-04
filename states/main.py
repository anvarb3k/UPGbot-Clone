from aiogram.dispatcher.filters.state import State, StatesGroup


class ShopState(StatesGroup):
    category = State()
    sub_category = State()
    product = State()
    amount = State()