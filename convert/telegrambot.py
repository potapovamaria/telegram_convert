import json

import jsonpickle
import telebot

from get_valute import *
URL_CONST = "https://www.cbr-xml-daily.ru/daily_json.js"
bot = telebot.TeleBot("1258265771:AAGfp0ILLF0Xjg34PcXn-wGOr2Qdgz7EA3I")

class TelegramBot:

    @bot.message_handler(commands=['start'])
    def start_message(message):
        value = " Привет, я Конвертер Валют!\n" + "\n" + "Я могу переводить белорусские рубли, доллар, евро, российские рубли, гривны по курсу.\n" + "Если вы хотите перевести одну из этих валют, напишите в соответствии с примером:\n\n" + "Русские рубли - /RUB\n" + "Евро - /EUR\n" + "Белорусские рубли - /BYN\n" + "Доллар - /USD\n" + "Гривны - /UAH\n" + "Для получения справки - /help\n"
        text = bot.send_message(message.chat.id, value)
        return json.loads(jsonpickle.encode(text))['text']

    @bot.message_handler(commands=['help'])
    def help_info(message):
        bot.send_message(message.chat.id, "/help - получение информации о командах\n"
                                          "/start - информация о самом боте\n"
                                          "/RUB - перевод из российских рублей в доступные валюты\n"
                                          "/EUR - перевод из евро в доступные валюты\n"
                                          "/USD - перевод из долларов в доступные валюты\n"
                                          "/BYN - перевод из белорусских рублей в доступные валюты\n"
                                          "/UAH - перевод из гривен в доступные валюты\n")

    @bot.message_handler(commands=['RUB'])
    def exchange_russia(message):
        rubles = bot.send_message(message.chat.id, "Введите количество российских рублей")
        bot.register_next_step_handler(rubles, TelegramBot.get_value_rub)

    def get_value_rub(message):
        string = message.text
        k = get_valute()
        answer = convert_rubles(string, k)
        if answer[1] == 0:
            bot.send_message(message.chat.id, answer)
            TelegramBot.exchange_russia(message)
        else:
            bot.send_message(message.chat.id, answer)

    @bot.message_handler(commands=['EUR'])
    def exchange_euro(message):
        eur = bot.send_message(message.chat.id, "Введите количество евро")
        bot.register_next_step_handler(eur, TelegramBot.get_value_eur)

    def get_value_eur(message):
        string = message.text
        k = get_valute()
        answer = convert_euro(string, k)
        if answer[1] == 0:
            bot.send_message(message.chat.id, answer)
            TelegramBot.exchange_euro(message)
        else:
            bot.send_message(message.chat.id, answer)

    @bot.message_handler(commands=['BYN'])
    def exchange_bel_rub(message):
        bel = bot.send_message(message.chat.id, "Введите количество белорусских рублей")
        bot.register_next_step_handler(bel, TelegramBot.get_value_bel_rub)

    def get_value_bel_rub(message):
        string = message.text
        k = get_valute()
        answer = convert_bel_rub(string, k)
        if answer[1] == 0:
            bot.send_message(message.chat.id, answer)
            TelegramBot.exchange_bel_rub(message)
        else:
            bot.send_message(message.chat.id, answer)

    @bot.message_handler(commands=['UAH'])
    def exchange_grivn(message):
        griv = bot.send_message(message.chat.id, "Введите количество гривен")
        bot.register_next_step_handler(griv, TelegramBot.get_value_grivn)

    def get_value_grivn(message):
        string = message.text
        k = get_valute()
        answer = convert_uah(string, k)
        if answer[1] == 0:
            bot.send_message(message.chat.id, answer)
            TelegramBot.exchange_grivn(message)
        else:
            bot.send_message(message.chat.id, answer)

    @bot.message_handler(commands=['USD'])
    def exchange_dollar(message):
        usd = bot.send_message(message.chat.id, "Введите количество долларов")
        bot.register_next_step_handler(usd, TelegramBot.get_value_usd)

    def get_value_usd(message):
        string = message.text
        k = get_valute()
        answer = convert_dollar(string, k)
        if answer[1] == 0:
            bot.send_message(message.chat.id, answer)
            TelegramBot.exchange_dollar(message)
        else:
            bot.send_message(message.chat.id, answer)

    @bot.message_handler(content_types=['photo'])
    def photo(message):
        bot.send_message(message.chat.id, "Извините, но я не могу смотреть фотографии")

    @bot.message_handler(content_types=['video'])
    def video(message):
        bot.send_message(message.chat.id, "Извините, но я не могу смотреть видео")

    @bot.message_handler(content_types=['sticker'])
    def sticker(message):
        bot.send_message(message.chat.id, "Извините, но я не понимаю команды" + '\n'
                                                                                "Воспользуйтесь /help, чтобы увидеть список доступных команд")

    @bot.message_handler(content_types=['voice'])
    def voice(message):
        bot.send_message(message.chat.id, "Извините, но я не могу слушать голосовые сообщения")

    @bot.message_handler(content_types=['text'])
    def echo(message):
        if message.text == 'help':
            TelegramBot.help_info(message)
            return
        if message.text == 'Help':
            TelegramBot.help_info(message)
            return
        if message.text == 'RUB':
            TelegramBot.exchange_russia(message)
            return
        if message.text == 'USD':
            TelegramBot.exchange_dollar(message)
            return
        if message.text == 'UAH':
            TelegramBot.exchange_grivn(message)
            return
        if message.text == 'BYN':
            TelegramBot.exchange_bel_rub(message)
            return
        if message.text == 'EUR':
            TelegramBot.exchange_grivn(message)
            return
        if message.text == 'Россия':
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJbdl-1KmObfKBaH3uu6-2Tg-VTghoWAAL2AAPXawQWz87rfPJo12YeBA')
        else:
            bot.send_message(message.chat.id, "Извините, но я не понимаю команды" + '\n'
                                                                                    "Воспользуйтесь /help, чтобы увидеть список доступных команд")
bot.polling(none_stop=True)
