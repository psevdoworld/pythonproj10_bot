import telebot # PyTelegramBotAPI == 4.20
from telebot.types import ReplyKeyboardRemove

from keyboards import yes_no_keyboard, get_category_keyboard, gen_markup

API_TOKEN = '6719564185:AAHJXsuQf5CwizlShPOzr5gSWGd6DiF8XcA'

bot = telebot.TeleBot(API_TOKEN)
bot.send_message(65353297,'hi i am alive',reply_markup=ReplyKeyboardRemove())

users = {
    65353297:'start',
    }


def is_in_shop(message):
    id = message.from_user.id
    if id in users:
        if users[id] == 'shop':
            return True
    return False
@bot.message_handler(func=is_in_shop) # когда функция запускается
def shop_message(message):
    if message.text=='аптечные':
        bot.send_message(message.chat.id,'а рецептик есть?')
    elif message.text=='овощи':
        bot.send_message(message.chat.id, 'осталась только редька',reply_markup=gen_markup('редька'))

    else:
        bot.send_message(message.chat.id, "Поздравляю вы застряли в магазине")

@bot.message_handler(func=lambda message: message.text=="да") # когда функция запускается
def yes_message(message):
    users[message.from_user.id] = 'shop'
    bot.reply_to(message, "Категорически согласен", reply_markup=get_category_keyboard()) # что функция делает

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Добро пожаловать, займемся покупками?", reply_markup=yes_no_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    message = call.message

    bot.send_message(65353297,f"""
    Начальника, человек {message.chat.id}
    хочет купить редьку""")

    if  "cb_yes" in call.data:
        item = call.data.strip('cb_yes_')
        bot.answer_callback_query(call.id, call.data)
        bot.send_message(message.chat.id, item+' кончилось')


bot.infinity_polling()