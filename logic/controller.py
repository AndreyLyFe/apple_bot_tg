from aiogram import types

import const.const
from db.db_connector import Database
import const.phrases as phrases
from const.const import *
from . import markups


class Controller:
    def __init__(self, bot):
        self.bot = bot
        #self.db = Database()

    async def command_start(self, message):
        name = message.from_user.first_name
        markup = markups.user_main_markup()
        text = phrases.phrase_for_start_first_greeting(
            data=dict(
                user_name=name
            )
        )
        return dict(text=text, markup=markup)

    async def message_main_menu_buttons_click(self, message):
        if message.text == const.const.NAME_OF_CATEGORY_BU['main_one_category']:
            text = phrases.answer_for_to_main_menu_one_button(
                data=dict(name_button=message.text)
            )
            markup = markups.one_category_from_main_menu()
            return dict(text=text, markup=markup)
        else:
            pass

    async def exit_to_main_menu(self):
        markup = markups.user_main_markup()
        text = phrases.answer_exit_to_main_menu()
        return dict(text=text, markup=markup)

    # Будущая ветка для iphone.
    # async def message_category_bu_buttons_click(self, message):
    #     if message.text == const.const.NAME_OF_CATEGORY_BU['categoty_iphone']:
    #         text = phrases.show_iphone()
    #         markup = markups.one_category_from_main_menu()
    #         return dict(text=text, markup=markup)
    #     else:
    #         pass
