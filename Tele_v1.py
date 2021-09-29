import datetime

import telebot

bot = telebot.TeleBot('')

new_a = 100
global mk_dict


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Я мало что умею, но буду учиться!")
    bot.send_message(message.chat.id,
                     "Доступные команды /start,\n/test,\n/diff,\n/mk_score_wr,\n/mk_score_r,\n/mk_score_clear")


@bot.message_handler(commands=['diff'])
def test_command(message):
    bot.send_message(message.chat.id, "Введите дату в формате DD.MM.YYYY")
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


@bot.message_handler(commands=['test'])
def sto_command(message):
    bot.send_message(message.chat.id, new_a)


@bot.message_handler(commands=['mk_score_wr'])
def test_command(message):
    bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(message, mk_score_name)


def mk_score_name(message):
    user = str(message.text)
    bot.send_message(message.chat.id, "Введите результат")
    bot.register_next_step_handler(message, mk_score_score, user)


def mk_score_score(message, user):
    score = int(str(message.text))
    user = user.upper()
    global mk_dict
    try:
        len(mk_dict)
    except:
        mk_dict = {}

    try:
        mk_dict[user] = mk_dict[user] + score
    except:
        mk_dict[user] = score
    bot.send_message(message.chat.id, f"Результат записан {user} - {score}")


@bot.message_handler(commands=['mk_score_r'])
def test_command(message):
    global mk_dict
    try:
        len(mk_dict)
    except:
        mk_dict = {}
    b = ''
    for x, y in mk_dict.items():
        a = x + ' ' + str(y)
        if len(b) == 0:
            b = a
        else:
            b = b + '\n' + a
    bot.send_message(message.chat.id, b)


@bot.message_handler(commands=['mk_score_clear'])
def test_command(message):
    global mk_dict
    try:
        mk_dict.clear()
        bot.send_message(message.chat.id, "Очищено")
    except:
        bot.send_message(message.chat.id, "Было пусто")
        pass


@bot.message_handler(content_types=['text'])
def text_command(message):
    bot.send_message(message.chat.id, "Я мало что умею, но буду учиться!")
    bot.send_message(message.chat.id, "Доступные команды /start, /test, /diff")


bot.polling(none_stop=True, interval=0)
