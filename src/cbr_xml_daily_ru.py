import datetime
import json
import requests
import os

# константы, Карл!
json_file_path = "currency_cbr_xml_daily.json"
# save_currency_path = 'currency.json'
request_from_web = "https://www.cbr-xml-daily.ru/daily_json.js"


def get_currency_rate(currency_name: str) -> float:
    data = request_and_cash()
    variants(data)
    currency_rate = parse_data(data, currency_name)


    return currency_rate


def save_to_json(currency_name: str, currency_rate: float, timedate: datetime,):
    """
    Словарь с данными о валюте, курсе и времени запроса
    в JSON файл
    """
    currency = {'currency_name': currency_name, 'currency_rate': currency_rate, 'datetime': str(timedate)}

    try:
        with open(json_file_path.json, 'w') as outfile:
            json.dump(currency, outfile)
            return True
    except FileNotFoundError:
        print(f"File \'{json_file_path}\' not found!")
        return False
    except Exception as e:
        print(f"Something went wrong. File: \'{json_file_path}\'; Error: {str(e)}")
        return False

def request_and_cash(forse_request: bool = False) -> list[str]:
    """
    Загружает JSON данные с сайта и пишет в файл.
    Если есть файл, то по умолчанию загружает из него.
    Возвращает JSON данные.
    """
    # константы, Карл!
    #save_currency_path = 'currency.json'
    request_from_web = "https://www.cbr-xml-daily.ru/daily_json.js"

    if os.path.exists(os.path.join(json_file_path)) and not forse_request:
        with open(json_file_path, "r") as read_file:
            data_json = json.load(read_file)
        # print(f"Загрузка из файла")
        # print(f"ДАННЫЕ \n {data_json}")
        return data_json

    else:
        try:
            response = requests.get(request_from_web)
            todos = json.loads(response.text)
            with open(json_file_path, 'w') as outfile:
                json.dump(todos, outfile)
            # print(f"Загрузка с сайта")
            # print(f"ДАННЫЕ \n {todos}")
            return todos
        except FileNotFoundError:
            # print(f"File \'{save_currency_path}\' not found!")
            return None
        except Exception as e:
            # print(f"Something went wrong. File: \'{save_currency_path}\'; Error: {str(e)}")
            return None


def parse_data(data: list[str], currency_name: str)-> float:
    # print(f"Курс: {data['Valute'][currency_name]['Value']}")
    return float(data['Valute'][currency_name]['Value'])

def variants(data: dict) -> list[str]:
    list_curency = []
    for currency in data['Valute']:
        # print(f"{currency}: ", end='')
        #
        # print(f"{data['Valute'][currency]['Nominal']} ", end='')
        # print(f"{data['Valute'][currency]['Name']} = ", end='')
        # print(f"{data['Valute'][currency]['Value']} RUB", end='\n')

        str1 = currency + ': ' + str(data['Valute'][currency]['Nominal']) + ' '
        str2 = data['Valute'][currency]['Name'] + ' = ' + str(data['Valute'][currency]['Value']) + ' RUB'

        list_curency.append(str1 + str2)
    return list_curency

        # print(str(currency['ID']))

        # print(f"{currency['CharCode']}: {currency['Nominal']} {currency['Name']} == {currency['Value']} RUB")
        # "AZN": {"ID": "R01020A", "NumCode": "944", "CharCode": "AZN", "Nominal": 1,
        #         "Name": "\u0410\u0437\u0435\u0440\u0431\u0430\u0439\u0434\u0436\u0430\u043d\u0441\u043a\u0438\u0439 \u043c\u0430\u043d\u0430\u0442",
        #         "Value": 53.3436, "Previous": 53.6726}



