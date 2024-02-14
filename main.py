#import datetime

from decouple import config
# from dotenv import load_dotenv
#import requests

#import os

from src.apilayer_currency import currency_now
from src.apilayer_currency import currency_list

from src.apilayer_currency import save_to_json_cash
from src.apilayer_currency import read_json_cash

# import telebot
#
# bot = telebot.TeleBot(config('TG_BOT_API_KEY'), parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
# bot.polling(none_stop=True, interval=0)
#
#
# # @bot.message_handler(content_types=['text'])
# # def get_text_messages(message):
# #     if message.text == "Привет":
# #         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
# #     elif message.text == "/help":
# #         bot.send_message(message.from_user.id, "Напиши привет")
# #     else:
# #         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# #     print(f"I do...")
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")
#
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

#
# def telebot_in_work(parameter):
#     api_key = config('TG_BOT_API_KEY')
#     print(api_key)
#
#     api_key = config('APILAYER_APIKEY')
#     print(api_key)
#
#     data: dict = {}
#
#     if parameter == 'apilayer':
#         data = currency_now(api_key, 'EUR', 'RUB')
#     elif parameter == 'apilayer_to_file':
#         data = currency_now(api_key, 'EUR', 'RUB')
#
#         if data is not None:
#             save_to_json_cash(data)
#         else:
#             print(f"Данные с сайта получить не удалось")
#     elif parameter == 'file':
#         data = read_json_cash()
#     elif parameter == 'list':
#         data = currency_list(api_key)
#     else:
#         print(f"неверный параметр")
#
#     data_in_bot = ''
#
#     for key, value in data.items():
#         if type(value) is dict:
#             data_in_bot += f'{key}:\n'
#             for key2, value2 in value.items():
#                 data_in_bot += f"  {key2}: {value2}"
#         else:
#             data_in_bot += f'{key}:  {value}'
#     return data_in_bot


def main():
    # load_dotenv()
    # database_url = config('DATABASE_URL')
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

            if data is not None:
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
            #telebot_in_work()
            print('telebot_in_work() ???')
        else:
            print(f"неверный параметр")

        for key, value in data.items():
            if type(value) is dict:
                print(f"{key}:")
                for key2, value2 in value.items():
                    print(f"  {key2}: {value2}")
            else:
                print(key, value, sep=': ')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
