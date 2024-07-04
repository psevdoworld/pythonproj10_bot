import telebot # PyTelegramBotAPI == 4.20
from telebot.types import ReplyKeyboardRemove

from backend import get_all_goods, like_by_id
from keyboards import yes_no_keyboard, get_category_keyboard, gen_markup

API_TOKEN = '6719564185:AAHJXsuQf5CwizlShPOzr5gSWGd6DiF8XcA'

bot = telebot.TeleBot(API_TOKEN)
#bot.send_message(65353297,'hi i am alive',reply_markup=ReplyKeyboardRemove())

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
        goods = get_all_goods()
        for good in goods:
            name = good["name"]
            cost = good['cost']
            likes = good['likes']
            good_id = good['id']
            text = f"Прекраснейшее {name} по цене всего {cost} рублей\nлайков у товара: {likes}"
            bot.send_message(message.chat.id, text ,reply_markup=gen_markup(good_id))

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
    if "cb_buy" in call.data:
        item = call.data.strip('cb_buy')
        bot.answer_callback_query(call.id,"покупаем" )

    if "cb_like" in call.data:
        item = call.data.strip('cb_like')
        from pprint import pprint
        pprint(call.__dict__)
        print(call.__dict__)
        like_by_id(item)
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        old_text = call.message.text
        old_text, likes = old_text.split(': ')
        print(repr(likes))
        likes = int(likes) + 1
        text = old_text + ': ' + str(likes)
        bot.edit_message_text(text, chat_id, message_id)
        bot.answer_callback_query(call.id, "ставим лайк")



bot.infinity_polling()