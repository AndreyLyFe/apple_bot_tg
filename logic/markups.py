from aiogram import types
import const.const


def user_main_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.row(types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['main_one_category']))
    markup.row(
        types.KeyboardButton("Second button"),
        types.KeyboardButton("Third button")
    )
    return markup

def one_category_from_main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=7, resize_keyboard=True)
    markup.row(
        types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['categoty_iphone']),
        types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['categoty_ipad'])
    )
    markup.row(
        types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['categoty_macbook']),
        types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['category_airpods'])
    )
    markup.row(
        types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['categoty_clock']),
        types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['categoty_devices'])
    )
    markup.row(types.KeyboardButton(text=const.const.NAME_OF_CATEGORY_BU['exit_to_main_menu']))
    return markup

