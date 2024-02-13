import datetime

from decouple import config
# from dotenv import load_dotenv
import requests


import os

from src.apilayer_currency import currency_now
from src.apilayer_currency import currency_list

from src.apilayer_currency import save_to_json_cash
from src.apilayer_currency import read_json_cash

import telebot;
bot = telebot.TeleBot('%ваш токен%');
# from src.apilayer_currency import currency_historical


def main2():
    pass
    # api_key = 'nCgAhGbEvs14xb15z2GJdVc0PsLvk1eq'
    # date = '2021-02-28'
    # print(currency_now(api_key))
    # print(f"\n")
    # print(currency_historical(api_key, date))

def telebot_in_work():
    while True:
        # print(f"Получить данные с сайта и записать в файл 'rw'")
        # print(f"Получить данные с сайта, в файл не писать 'r'")
        # print(f"Получить список валют с сайта 'l'")
        # print(f"Получить данные или из файла 'f'")
        print(f"Работа с ботом telegram 't'")
        print(f"Выход 'q'")

        parameter = input('Введите команду: ')
        if parameter == 't':

            # data = currency_now(api_key, 'EUR', 'RUB')
        # elif parameter == 'rw':
        #     data = currency_now(api_key, 'EUR', 'RUB')
        #
        #     if (data is not None):
        #         save_to_json_cash(data)
        #     else:
        #         print(f"Данные с сайта получить не удалось")
        # elif parameter == 'f':
        #     data = read_json_cash()
        elif parameter == 'q':
            break
        # elif parameter == 'l':
        #     data = currency_list(api_key)
        # elif parameter == 't':
        #     data = currency_list(api_key)
        else:
            print(f"неверный параметр")

        for key, value in data.items():
            if type(value) is dict:
                print(f"{key}:")
                for key, value in value.items():
                    print(f"  {key}: {value}")
            else:
                print(key, value, sep=': ')


def main():
    # load_dotenv()
    #database_url = config('DATABASE_URL')
    api_key = config('APILAYER_APIKEY')
    print(api_key)
    data: dict = {}

    while True:
        print(f"Получить данные с сайта и записать в файл 'rw'")
        print(f"Получить данные с сайта, в файл не писать 'r'")
        print(f"Получить список валют с сайта 'l'")
        print(f"Получить данные или из файла 'f'")
        print(f"Работа с ботом telegram 't'")
        print(f"Выход 'q'")
        parameter = input('Введите параметр: ')
        if parameter == 'r':
            data = currency_now(api_key, 'EUR', 'RUB')
        elif parameter == 'rw':
            data = currency_now(api_key, 'EUR', 'RUB')

            if (data is not None):
                save_to_json_cash(data)
            else:
                print(f"Данные с сайта получить не удалось")
        elif parameter == 'f':
            data = read_json_cash()
        elif parameter == 'q':
            break
        elif parameter == 'l':
            data = currency_list(api_key)
        elif parameter == 't':
            data = currency_list(api_key)
        else:
            print(f"неверный параметр")


        for key, value in data.items():
            if type(value) is dict:
                print(f"{key}:")
                for key, value in value.items():
                    print(f"  {key}: {value}")
            else:
                print(key, value, sep=': ')




if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
