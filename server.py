import logging
import os
import markups
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
import realty
from pprint import pprint

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

chosen_option = ''
realty_option_chosen = False
realty = realty.Realty()


# Главное меню
@dp.message_handler(commands=['start'])
@dp.message_handler(Text(equals='Главное меню'))
async def start(message: types.Message):
    await message.answer('Выберите одну из услуг', reply_markup=markups.welcome_menu)


# Главное меню
@dp.callback_query_handler(text='back_to_welcome_btn')
async def start2(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, 'Выберите одну из услуг', reply_markup=markups.welcome_menu)


# Раздел "Недвижимость": меню
@dp.message_handler(commands=['realty'])
@dp.callback_query_handler(text='welcome_btn_realty')
@dp.callback_query_handler(text='back_to_realty_btn')
async def show_realty_menu(message: types.Message):
    realty.form_user(message['from']['id'],
                     message['from']['username'],
                     message['from']['first_name'],
                     message['from']['last_name'])
    # await message.answer('realty', reply_markup=markups.welcome_menu)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, '<b>Раздел "Недвижимость"</b>\nВыберите одну из опций',
                           reply_markup=markups.realty_menu)


# Раздел "Недвижимость": ввод кадастрового номера
@dp.callback_query_handler(text_contains='realty_btn')
async def show_realty_options(call: types.CallbackQuery):
    global realty_option_chosen, chosen_option
    realty_option_chosen = True
    chosen_option = call.data

    await bot.delete_message(call.from_user.id, call.message.message_id)
    print(call.data)

    breadcrumb = '<b>Раздел "Недвижимость" - '
    if call.data == 'realty_btn_dispute_cad_cost':
        breadcrumb += 'Оспорить кадастровую стоимость</b>\n'
    if call.data == 'realty_btn_order_flat_check':
        breadcrumb += 'Заказать проверку квартиры</b>\n'
    if call.data == 'realty_btn_exclude_700':
        breadcrumb += 'Исключить из Перечня (700 ПП)</b>\n'
    if call.data == 'realty_btn_exclude_819':
        breadcrumb += 'Исключить из Самостроя (819 ПП)</b>\n'

    await bot.send_message(call.from_user.id, breadcrumb + 'Введите кадастровый номер',
                           reply_markup=markups.back_to_realty_menu)


# Глобальная функция, обрабатывающая текстовый ввод
@dp.message_handler()
async def use_global_switcher(message: types.Message):
    global realty_option_chosen
    if realty_option_chosen:
        realty_option_chosen = False
        await bot.send_message(message.from_user.id,
                               f'''<b>Введённый кадастровый номер: {message.text}</b>
Ваша заявка отправлена. В ближайшее время мы свяжемся с Вами в Telegram.
Благодарим Вас за обращение!''',
                               reply_markup=markups.back_to_welcome_menu)
        realty.form_request(message, chosen_option)
        await bot.send_message(1027909953, 'New request')
        print(realty.find_request())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
