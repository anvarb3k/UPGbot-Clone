import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import bot, db, dp

from keyboards.inline.main_menu import main


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    # name = message.from_user.full_name
    await state.finish()
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(tg_id=message.from_user.id, full_name=message.from_user.full_name, username=message.from_user.username)
        await message.answer(f"Xush kelibsiz! {message.from_user.full_name}", reply_markup=main)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{message.from_user.full_name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {message.from_user.full_name}", reply_markup=main)
