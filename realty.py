import datetime
import requests
import random
from db import DB


def get_cad_object():
    try:
        r = requests.get('')
        data = r.json()
    except Exception:
        print('Error')


class Realty:
    db = DB()

    def form_request(self, chosen_option):
        get_cad_object()
        test_cad_obj = {'cad_num': random.randint(1000000, 1999999),
                        'address': f'Москва, ул. Тверская, д.{random.randint(1, 15)}',
                        'owners_amount': random.randint(1, 5),
                        'cad_cost': random.randint(1000000, 5000000)}
        present_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if chosen_option == 'realty_btn_dispute_cad_cost':
            self.db.insert_request(
                'Недвижимость',
                'Оспорить кадастровую стоимость',
                present_time,
                test_cad_obj)
        if chosen_option == 'realty_btn_order_flat_check':
            self.db.insert_request(
                'Недвижимость',
                'Заказать проверку квартиры',
                present_time,
                test_cad_obj)
        if chosen_option == 'realty_btn_exclude_700':
            self.db.insert_request(
                'Недвижимость',
                'Исключить из Перечня (700 ПП)',
                present_time,
                test_cad_obj)
        if chosen_option == 'realty_btn_exclude_819':
            self.db.insert_request(
                'Недвижимость',
                'Исключить из Самостроя (819 ПП)',
                present_time,
                test_cad_obj)

    def form_user(self, tg_id, username, first_name, last_name):
        if not self.db.find_user_by_tg_id(tg_id):
            self.db.insert_user(tg_id, username, first_name, last_name)
            print('User inserted into "users" table')