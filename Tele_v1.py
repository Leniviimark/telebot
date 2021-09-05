import datetime

import telebot

bot = telebot.TeleBot('1975403441:AAGHW_PopX4Yw70x23S6juXZLrK3GuL9cgE')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Я нихрена не умею, но буду учиться!")
    bot.send_message(message.chat.id, "Доступные команды /start, /test, /diff")


@bot.message_handler(commands=['test'])
def test_command(message):
    bot.send_message(message.chat.id, "Чего желаете?")


@bot.message_handler(commands=['diff'])
def test_command(message):
    bot.send_message(message.chat.id, "Ведите предстоющую дату в формате DD.MM.YYYY")
    bot.register_next_step_handler(message, diff_date)


def diff_date(message):
    a = message.text
    b = datetime.date.today()
    c = datetime.datetime.strptime(a, '%d.%m.%Y')
    c = datetime.datetime.date(c)
    d = c - b
    bot.send_message(message.from_user.id, f'{d.days} дней')
    # bot.register_next_step_handler(message, get_surname)


@bot.message_handler(content_types=['text'])
def text_command(message):
    bot.send_message(message.chat.id, "Я нихрена не умею, но буду учиться!")
    bot.send_message(message.chat.id, "Доступные команды /start, /test, /diff")


bot.polling(none_stop=True, interval=0)
