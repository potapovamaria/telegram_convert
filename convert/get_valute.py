import json

import requests

URL_CONST = "https://www.cbr-xml-daily.ru/daily_json.js"

def get_valute():
    response = requests.get(URL_CONST)
    valutes = json.loads(response.text)
    global dollar, bel_rub, grivn, euro
    dollar = valutes['Valute']['USD']['Value']
    bel_rub = valutes['Valute']['BYN']['Value']
    grivn = valutes['Valute']['UAH']['Value']
    euro = valutes['Valute']['EUR']['Value']
    return dollar, bel_rub, grivn, euro

def convert_rubles(string, k):
    try:
        rubles = float(string)
        if rubles <= 0:
            return "Вы не можете вводить неположительное число", 0
        else:
            stringValute = "USD  " + str(round(rubles / k[0], 2)) + '\n' + "BYN  " + str(round(rubles / k[1], 2)) + '\n' + "UAH  " + str(round(rubles / k[2], 2)) + '\n' + "EUR  " + str(round(rubles / k[3], 2)) + '\n'
            return stringValute, 1
    except ValueError:
        return "Это должно быть положительное число", 0

def convert_euro(string, k):
    try:
        eur = float(string)
        if eur <= 0:
            return "Вы не можете вводить неположительное число", 0
        else:
            stringValute = "USD  " + str(round(k[3] * eur / k[0], 2)) + '\n' + "BYN  " + str(round(k[3] * eur / k[1], 2)) + '\n' + "UAH  " + str(round(k[3] * eur / k[2], 2)) + '\n' +  "RUB  " + str(round(k[3] * eur, 2)) + '\n'
            return stringValute, 1
    except ValueError:
        return "Это должно быть положительное число", 0


def convert_bel_rub(string, k):
    try:
        bel = float(string)
        if bel <= 0:
            return "Вы не можете вводить неположительное число", 0
        else:
            stringValute = "USD  " + str(round(k[1] * bel / k[0], 2)) + '\n' + "EUR  " + str(round(k[1] * bel / k[3], 2)) + '\n' + "UAH  " + str(round(k[1] * bel / k[2], 2)) + '\n' + "RUB  " + str(round(k[1] * bel, 2)) + '\n'
            return stringValute, 1
    except ValueError:
        return "Это должно быть положительное число", 0

def convert_uah(string, k):
    try:
        griv = float(string)
        if griv <= 0:
            return "Вы не можете вводить неположительное число", 0
        else:
            stringValute = "USD  " + str(round(griv * k[2] / k[0], 2)) + '\n' + "BYN  " + str(round(griv * k[2] / k[1], 2)) + '\n' + "EUR  " + str(round(griv * k[2] / k[3], 2)) + '\n' + "RUB  " + str(round(griv * k[2], 2)) + '\n'
            return stringValute, 1
    except ValueError:
        return "Это должно быть положительное число", 0

def convert_dollar(string, k):
    try:
        usd = float(string)
        if usd <= 0:
            return "Вы не можете вводить неположительное число", 0
        else:
            stringValute = "UAH  " + str(round(usd * k[0] / k[2], 2)) + '\n' + "BYN  " + str(round(usd * k[0] / k[1], 2)) + '\n' + "EUR  " + str(round(usd * k[0] / k[3], 2)) + '\n' + "RUB  " + str(round(usd * k[0], 2)) + '\n'
            return stringValute, 1
    except ValueError:
        return "Это должно быть положительное число", 0
