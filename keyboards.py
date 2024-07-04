from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

yes_no_keyboard = ReplyKeyboardMarkup(row_width=1)

yes_no_keyboard.add(
    KeyboardButton('да'),
    KeyboardButton('нет'),
)

def get_category_keyboard():
    categories = ['аптечные', 'овощи']
    k = ReplyKeyboardMarkup(row_width=1)
    for cat in categories:
        k.add(KeyboardButton(cat))
    return k

def gen_markup(item_name):
    markup = InlineKeyboardMarkup(row_width = 2)
    markup.add(
        InlineKeyboardButton("да", callback_data="cb_yes_"+item_name),
        InlineKeyboardButton("нет", callback_data="cb_no_"+item_name),
    )
    return markup