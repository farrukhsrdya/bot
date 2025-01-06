import telebot
import buttons, database
from geopy import Photon
geolocator = Photon(user_agent='geo_locator', timeout=10)

bot = telebot.TeleBot('7915137454:AAGxTF39CoY9xzzIamv7XXIPDQZYh9qjApc')



@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    user_id = message.from_user.id
    if database.check_user(user_id):
        name =  database.check_user(user_id)
        bot.send_message(user_id, f'Добро пожаловать, {name[1]}!')
    else:
        bot.send_message(user_id, 'Привет Давай начнем регистрацию\nНапиши свое имя',
                         reply_markup=telebot.types.ReplyKeyboardRemove())

        bot.register_next_step_handler(message, get_name)



@bot.message_handler(content_types=['text'])

def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично Тепер отправь свой номер',
                     reply_markup=buttons.num_button())

    bot.register_next_step_handler(message, get_num, user_name)



def get_num(message, user_name):
    user_id = message.from_user.id

    if message.contact:
        user_num = message.contact.phone_number
        bot.send_message(user_id, 'Отправьте локацию ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_location, user_name, user_num)

    else:
        bot.send_message(user_id, 'Отправьте контакт по кнопке или через скрепку!')
        bot.register_next_step_handler(message, get_num)


def get_location(message,user_name, user_num):
    user_id = message.from_user.id
    if message.location:
        user_tt = message.location
        addres = geolocator.reverse((user_tt.latitude, user_tt.longitude)).address
        database.register(user_id, user_name, user_num, addres)
        bot.send_message(user_id, 'Регистрация Закончилась',
                         reply_markup=telebot.types.ReplyKeyboardRemove())


bot.polling(non_stop=True)









