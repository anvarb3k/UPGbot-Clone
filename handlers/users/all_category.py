from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db, dp
from states.main import ShopState

from keyboards.inline.main_menu import back, home


@dp.callback_query_handler(text="all_product")
async def allcaty(call: types.CallbackQuery):
    caty_info = db.select_all_caty()
    markup = InlineKeyboardMarkup(row_width=2)
    for caty in caty_info:
        markup.insert(InlineKeyboardButton(text=caty[1], callback_data=caty[2]))
    markup.add(back, home)
    await call.message.answer("Barcha mahsulotlar royhati", reply_markup=markup)
    await ShopState.category.set()

@dp.callback_query_handler(state=ShopState.category)
async def get_sub_caty(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    slug = call.data
    caty_info = db.get_caties_info(slug=slug)
    caty_id = caty_info[0]
    caty_title = caty_info[1]
    caty_image = caty_info[3]
    sub_catys = db.select_all_caty_by_sub_id(category_id=caty_id)
    markup = InlineKeyboardMarkup(row_width=2)
    for sub_caty in sub_catys:
        markup.insert(InlineKeyboardButton(text=sub_caty[0], callback_data=sub_caty[1]))
    markup.add(back, home)
    await call.message.answer_photo(photo=caty_image, caption=f"Siz {caty_title} bo'limidasiz", reply_markup=markup)
    await ShopState.next()
