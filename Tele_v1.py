import datetime

import telebot

bot = telebot.TeleBot('1975403441:AAGHW_PopX4Yw70x23S6juXZLrK3GuL9cgE')

new_a = 100


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Я мало что умею, но буду учиться!")
    bot.send_message(message.chat.id, "Доступные команды /start, /test, /diff")


@bot.message_handler(commands=['diff'])
def test_command(message):
    bot.send_message(message.chat.id, "Ведите дату в формате DD.MM.YYYY")
    bot.register_next_step_handler(message, diff_date)


def diff_date(message):
    a = message.text
    b = datetime.datetime.now()
    c = datetime.datetime.strptime(a, '%d.%m.%Y')
    # c = datetime.datetime.date(c)
    d = c - b
    if d.days < 0:
        bot.send_message(message.from_user.id,
                         'Прошло ' + str(-d.days) + ' days ' + str(d.seconds // 3600) + ' hours ' + str(
                             d.seconds % 3600 // 60) + ' minutes ' + str(
                             d.seconds % 60) + ' seconds')
    else:
        bot.send_message(message.from_user.id,
                         'Осталось ' + str(d.days) + ' days ' + str(d.seconds // 3600) + ' hours ' + str(
                             d.seconds % 3600 // 60) + ' minutes ' + str(
                             d.seconds % 60) + ' seconds')

    # bot.register_next_step_handler(message, get_surname)


@bot.message_handler(content_types=['text'])
def text_command(message):
    bot.send_message(message.chat.id, "Я мало что умею, но буду учиться!")
    bot.send_message(message.chat.id, "Доступные команды /start, /test, /diff")


@bot.message_handler(commands=['test'])
def sto_command(message):
    bot.send_message(message.chat.id, new_a)


bot.polling(none_stop=True, interval=0)
