import datetime
import json
import requests
import os

json_file_path = "apilayer_currency.json"
base_url = "https://api.apilayer.com/currency_data"

def currency_now(api_key, source, currency) -> str | None:
    """
    Получите курсы валюты currency относительно source c сайта https://api.apilayer.com.
    """
    url = base_url + "/live?source=" + source + "&currencies=" + currency

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()

    if status_code == 200:
        #print(f"response.status_code= {status_code}")
        return result
    else:
        print(f"response.status_code= {status_code}")
        print(f"response.text= {result}")
        return None


# def currency_historical(api_key, date):
#     """
#     Настройте получение курсов валют на определенную дату.
#     ATTENTION! Дата идет в формате ХХХХ-ХХ-ХХ, год-месяц-число
#     """
#     # валюта, которая берется за основу
#     source = 'EUR'
#     # курс относительно валют (можно хоть все через запятую, которые есть)
#     currencies = 'RUB,USD,KZT'
#
#     # url = "https://api.apilayer.com/currency_data/historical?date=" + date
#     url = "https://api.apilayer.com/currency_data/historical?date=" + date + "&source=" + source + "&currencies=" + currencies
#
#     payload = {}
#     headers = {
#         "apikey": api_key
#     }
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#
#     status_code = response.status_code
#     result = response.text
#
#     return result

def save_to_json_cash(json_data: list)-> bool:
    """
    Словарь с данными о валюте, курсе и времени запроса
    в JSON файл
    """
    try:
        with open(json_file_path, 'w') as outfile:
            json.dump(json_data, outfile)
            return True
    except FileNotFoundError:
        print(f"File \'{json_file_path}\' not found!")
        return False
    except Exception as e:
        print(f"Something went wrong. File: \'{json_file_path}\'; Error: {str(e)}")
        return False

def currency_list(api_key):
    url = base_url + "/list"

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()

    if status_code == 200:
        #print(f"response.status_code= {status_code}")
        return result
    else:
        print(f"response.status_code= {status_code}")
        print(f"response.text= {result}")
        return None

def read_json_cash() -> list[str] | None:
    """
    Читает кэшированные данные, если есть. Если нет или не читаются - возвращает NULL
    """
    data_json = []
    try:
        if os.path.exists(os.path.join(json_file_path)):
            with open(json_file_path, "r") as read_file:
                data_json = json.load(read_file)

            # print(f"Загрузка из файла {json_file_path}")
            # print(f"ДАННЫЕ \n {data_json}")

        return data_json
    except FileNotFoundError:
        print(f"File \'{json_file_path}\' not found!")
        return None
    except Exception as e:
        print(f"Something went wrong. File: \'{json_file_path}\'; Error: {str(e)}")
        return None

def request_and_cash(forse_request: bool = False) -> list[str]:
    """
    Загружает JSON данные с сайта и пишет в файл.
    Если есть файл, то по умолчанию загружает из него.
    Возвращает JSON данные.
    """
    # константы, Карл!
    save_currency_path = 'currency.json'
    request_from_web = "https://www.cbr-xml-daily.ru/daily_json.js"

    if os.path.exists(os.path.join(save_currency_path)) and not forse_request:
        with open(save_currency_path, "r") as read_file:
            data_json = json.load(read_file)
        # print(f"Загрузка из файла")
        # print(f"ДАННЫЕ \n {data_json}")
        return data_json

    else:
        try:
            response = requests.get(request_from_web)
            todos = json.loads(response.text)
            with open(save_currency_path, 'w') as outfile:
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
