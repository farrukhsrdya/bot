from telebot import types


def num_button():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num = types.KeyboardButton('Отправит номер', request_contact=True)

    kb.add(num)

    return kb




def tt_button():

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    tt = types.KeyboardButton(text='Отправить местоположение', request_location=True)

    keyboard.add(tt)

    return keyboard






