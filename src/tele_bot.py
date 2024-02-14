import telebot
from src.apilayer_currency import currency_now
from src.apilayer_currency import currency_list

from src.apilayer_currency import save_to_json_cash
from src.apilayer_currency import read_json_cash
from decouple import config

bot = telebot.TeleBot(config('TELERGAM_BOT_API'))


@bot.message_handler(commands=['start', 'stop'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    commands_list = """
    /apilayer - Получить данные с сайта, в файл не писать
/apilayer_to_file - Получить данные с сайта и записать в файл
/file - Получить данные или из файла
/list - Получить список валют с сайта
    """

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, commands_list)
    elif message.text == "/file": # ['/apilayer', '/apilayer_to_file', '/file', '/list']:
        data: dict = {}
        data = read_json_cash()
        data_in_bot = ''

        for key, value in data.items():
            if type(value) is dict:
                data_in_bot += f'{key}:\n'
                for key2, value2 in value.items():
                    data_in_bot += f"  {key2}: {value2}\n"
            else:
                data_in_bot += f'{key}:  {value}\n'

        # print(telebot_in_work(str(message.text)))
        bot.send_message(message.from_user.id, '!!!!!!!!!!!!!!!!!!')
        bot.send_message(message.from_user.id, str(data_in_bot))
    elif message.text == "/list":
        bot.send_message(message.from_user.id, telebot_in_work("/list"))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    print(f"I do...")


@bot.message_handler(commands=['apilayer', 'apilayer_to_file', 'file', 'list'])
def send_currency(message):
    bot.reply_to(message, telebot_in_work(message.text))




@bot.message_handler(commands=['apilayer', 'apilayer_to_file', 'file', 'list'])
def telebot_in_work(parameter):
    api_key = config('TG_BOT_API_KEY')
    print(api_key)

    api_key = config('APILAYER_APIKEY')
    print(api_key)

    data: dict = {}

    if parameter == '/apilayer':
        data = currency_now(api_key, 'EUR', 'RUB')
    elif parameter == '/apilayer_to_file':
        data = currency_now(api_key, 'EUR', 'RUB')

        if data is not None:
            save_to_json_cash(data)
        else:
            print(f"Данные с сайта получить не удалось")
    elif parameter == '/file':
        data = read_json_cash()
    elif parameter == '/list':
        data = currency_list(api_key)
    else:
        print(f"неверный параметр")

    data_in_bot = ''

    for key, value in data.items():
        if type(value) is dict:
            data_in_bot += f'{key}:\n'
            for key2, value2 in value.items():
                data_in_bot += f"  {key2}: {value2}\n"
        else:
            data_in_bot += f'{key}:  {value}\n'
    return data_in_bot


bot.infinity_polling()