# Telegram bot converter

# Проблема
<br />
<br /> На сайте Центрального Банка России отсутствует конвертер валют, только курс, что делает невозможным конвертацию валют в автоматическом режиме, используя данные с этого сайта. Необходимо искать дополнительные средства для этого. Наш проект дает такую возможность.

# Требования
<br /> Проект реализован на языке Python с использование библиотеки PyTelegramBotAPI.
<br />Проект должен соответствовать следующей диаграмме:
 ![Image alt](https://github.com/potapovamaria/telegram_convert/blob/master/convert/img/img1.png)

# Разработка архитектуры и детальное проектирование
<br />1)	Контекстная диаграмма
<br /> ![Image alt](https://github.com/potapovamaria/telegram_convert/blob/master/convert/img/img2.png)
<br />2)	Контейнерная диаграмма
<br /> ![Image alt](https://github.com/potapovamaria/telegram_convert/blob/master/convert/img/img3.png)

# Кодирование и отладка
<br />Проект написан на языке программирования Python в среде разработки PyCharm. Сервер был развернут локально.

# Тестирование 
<br />Был выполнен ряд тестов, написанных с помощью фреймворка автоматического тестирования unittest.

# Сборка проекта
<br />1)	Запуск тестов: python -m unittest discover
<br />2)	Сборка и запуск приложения: python telegrambot.py
