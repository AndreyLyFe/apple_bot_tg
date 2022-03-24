import const.const
from .controller import Controller
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from os import getenv
import const.phrases

#! temp
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=getenv("BOT_TOKEN"))
Bot.set_current(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
c = Controller(bot=bot)


@dp.message_handler(commands='start')
async def command_start_process(message: types.Message):
    response = await c.command_start(message=message)
    await message.reply(
        text=response["text"],
        reply_markup=response["markup"],
        parse_mode="HTML",
        reply=False
    )

@dp.message_handler(lambda message: message.text == const.const.NAME_OF_CATEGORY_BU['main_one_category'])
async def message_main_menu_buttons_click_process(message: types.Message):
    response = await c.message_main_menu_buttons_click(message=message)
    await message.reply(
        text=response["text"],
        parse_mode="HTML",
        reply=False,
        reply_markup=response['markup']
        )




#При нажатие кнопки "Главное меню" выбрасывает в корень бота
@dp.message_handler(lambda message: message.text == const.const.NAME_OF_CATEGORY_BU['exit_to_main_menu'])
async def exit_to_main_menu(message: types.Message):
    response = await c.command_start(message=message)
    await message.reply(
        reply_markup=response["markup"],
        parse_mode="HTML",
        reply=False,
        text=const.phrases.answer_exit_to_main_menu()
    )








#Будущая ветка для iphone.
# @dp.message_handler(lambda message: message.text == const.const.NAME_OF_CATEGORY_BU['categoty_iphone'])
# async def message_iphone_button_click(message: types.Message):
#     response = await c.message_main_menu_buttons_click(message=message)
#     await message.reply(
#         text=response["text"],
#         parse_mode="HTML",
#         reply=False,
#         reply_markup=response['markup']
#     )

    