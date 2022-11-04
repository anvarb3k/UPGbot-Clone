from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Barcha mahsulotlar", callback_data="all_product")],
        [
            InlineKeyboardButton(text="Savatcha", callback_data="cart"),
            InlineKeyboardButton(text="Orders", callback_data="orders")
        ],
        [
            InlineKeyboardButton(text="Search", callback_data="search"),
            InlineKeyboardButton(text="Settings", callback_data="settings")
        ]
    ]
)

back = InlineKeyboardButton(text="Orqaga", callback_data="back")
home = InlineKeyboardButton(text="Bosh sahifa", callback_data="home")