import telebot
from main_TG import Desk, Column, Task

bot = telebot.TeleBot('5815075362:AAGFnc0bNO-u15cl2TLqY8jI-DPG_2mNETs')

default_column = Column([], 'box')
default_desk = Desk([], '')
user_desks = []


# General
@bot.message_handler(commands=['info'])
def get_info(message):
    bot.send_message(message.from_user.id,
                     "Ты (с)можешь организовать свои задачи!\n")


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.from_user.id,
                     "  /info - краткая информация о боте\n  /help - данный список")


def incorrect_input(message):
    bot.send_message(message.from_user.id,
                     "Неправильный ввод, пожалуйста попробуй ещё раз")


# Desk
@bot.message_handler(commands=['createdesk'])  # createdesk <desk>
def create_desk(message):
    args = message.text.split()
    if len(args) != 2:
        incorrect_input(message)
        return
    name_desk = args[1]
    user_desks.append(Desk([], name_desk))
    bot.send_message(message.from_user.id, "Ты создал доску " + str(name_desk))
    global default_desk
    if not default_desk:
        default_desk = user_desks[0]


@bot.message_handler(commands=['setdefaultdesk'])  # setdefaultdesk <desk>
def set_default_desk(message):
    args = message.text.split()
    if len(args) != 2 or args[1] not in user_desks:
        incorrect_input(message)
        return
    global default_desk
    default_desk = user_desks[user_desks.index(args[1])]
    bot.send_message(message.from_user.id,
                     "Теперь доска по умолчанию: " + str(default_desk))


@bot.message_handler(commands=['deletedesk'])  # deletedesk <desk>
def delete_desk(message):
    name_desk = message.text.split()[1]
    if name_desk not in user_desks or name_desk == default_desk:
        incorrect_input(message)
        return

    user_desks.pop(user_desks.index(name_desk))
    bot.send_message(message.from_user.id, "Доска " +
                     str(name_desk) + " удалена!\n")


@bot.message_handler(commands=['showdesks'])  # showdesks
def show_desks(message):
    if not user_desks and len(message.text) != 1:
        incorrect_input(message)
        return
    bot.send_message(message.from_user.id, '\n'.join(map(str, user_desks)))
    bot.send_message(message.from_user.id,
                     "Доска по умолчанию " + default_desk.name)

# Column


# setdefaultcolumn <desk> <column>

@bot.message_handler(commands=['createcolumn'])  # createcolumn <desk> <column>
def create_column(message):
    args = message.text.split()
    if len(args) != 3:
        incorrect_input(message)
        return

    name_desk = args[1]
    name_column = args[2]

    new_column = Column([], name_column)
    user_desks[user_desks.index(name_desk)].add_column(new_column)
    bot.send_message(message.from_user.id,
                     "Ты создал колону " + str(new_column.name) + '\n')

    global default_column
    if default_desk == user_desks[user_desks.index(name_desk)]:
        default_column = default_desk.columns[0]


# setdefaultcolumn <desk> <column>
@bot.message_handler(commands=['setdefaultcolumn'])
def set_default_column(message):
    args = message.text.split()
    if len(args) == 3:
        current_desk = args[1]
        current_column = args[2]
    else:
        incorrect_input(message)
        return
    global default_column

    default_column = user_desks[user_desks.index(current_desk)][current_column]

    bot.send_message(message.from_user.id,
                     "Теперь колонна по умолчанию: " + str(default_column))


@bot.message_handler(commands=['deletecolumn'])  # deletecolumn <desk> <column>
def delete_column_from_desk(message):
    args = message.text.split()
    if len(args) == 3:
        current_desk = args[1]
        current_column = args[2]
    else:
        incorrect_input(message)
        return
    bot.send_message(message.from_user.id, "Колонна " +
                     str(current_column) + " удалена из " + str(current_desk))


@bot.message_handler(commands=['showcolumns'])  # showcolumns <desk>
def show_columns(message):
    args = message.text.split()
    if len(args) != 2 or args[1] not in user_desks:
        incorrect_input(message)
        return
    current_desk = args[1]
    bot.send_message(message.from_user.id, '\n'.join(
        map(str, user_desks[user_desks.index(current_desk)].columns)))
    bot.send_message(message.from_user.id,
                     "Колонна по умолчанию " + default_column.name)


# Task
@bot.message_handler(commands=['showtasks'])  # showtasks <desk> <column>
def show_tasks(message):
    args = message.text.split()
    if len(args) != 3:
        incorrect_input(message)
        return
    name_desk = args[1]
    name_column = args[2]

    bot.send_message(message.from_user.id,
                     '\n'.join(map(str, user_desks[user_desks.index(name_desk)][name_column].tasks)))


@bot.message_handler(func=lambda message: True)
def get_tasks(message):
    args = message.text.split()
    if args[0][0] == '/':
        incorrect_input(message)
        return

    task = Task(message.text)
    user_desks[user_desks.index(default_desk)
               ][default_column.name].add_task(task)


bot.polling()
