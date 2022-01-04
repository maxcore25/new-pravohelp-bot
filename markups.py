from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
welcome_menu = InlineKeyboardMarkup(row_width=1)
welcome_btn_realty = InlineKeyboardButton(text='Недвижимость', callback_data='welcome_btn_realty')
# welcome_btn_arbitration = InlineKeyboardButton(text='Арбитраж', callback_data='welcome_btn_arbitration')
# welcome_btn_tax_service = InlineKeyboardButton(text='Налоговая', callback_data='welcome_btn_tax_service')
welcome_instruction = InlineKeyboardButton(text='Инструкция', callback_data='welcome_instruction')
welcome_menu.insert(welcome_btn_realty)
# welcome_menu.insert(welcome_btn_arbitration)
# welcome_menu.insert(welcome_btn_tax_service)
welcome_menu.insert(welcome_instruction)

# Раздел "Недвижимость": меню
realty_menu = InlineKeyboardMarkup(row_width=2)
realty_btn_dispute_cad_cost = InlineKeyboardButton(text='Оспорить кадастровую стоимость',
                                                   callback_data='realty_btn_dispute_cad_cost')
realty_btn_order_flat_check = InlineKeyboardButton(text='Заказать проверку квартиры',
                                                   callback_data='realty_btn_order_flat_check')
realty_btn_exclude_700 = InlineKeyboardButton(text='Исключить из Перечня (700 ПП)',
                                              callback_data='realty_btn_exclude_700')
realty_btn_exclude_819 = InlineKeyboardButton(text='Исключить из Самостроя (819 ПП)',
                                              callback_data='realty_btn_exclude_819')
back_to_welcome_btn = InlineKeyboardButton(text='« Назад', callback_data='back_to_welcome_btn')
realty_menu.insert(realty_btn_dispute_cad_cost)
realty_menu.insert(realty_btn_order_flat_check)
realty_menu.insert(realty_btn_exclude_700)
realty_menu.insert(realty_btn_exclude_819)
realty_menu.insert(back_to_welcome_btn)

# Раздел "Недвижимость": Кнопка "Назад" на меню "Недвижимость"
back_to_realty_menu = InlineKeyboardMarkup(row_width=1)
back_to_realty_btn = InlineKeyboardButton(text='« Назад', callback_data='back_to_realty_btn')
back_to_realty_menu.insert(back_to_realty_btn)

# Кнопка "Главное меню"
back_to_welcome_menu = InlineKeyboardMarkup(row_width=1)
back_to_welcome_btn = InlineKeyboardButton(text='Главное меню', callback_data='back_to_welcome_btn')
back_to_welcome_menu.insert(back_to_welcome_btn)
