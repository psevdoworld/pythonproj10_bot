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

def gen_markup(item_id):
    markup = InlineKeyboardMarkup(row_width = 2)
    markup.add(
        InlineKeyboardButton("купить", callback_data=f"cb_buy_{item_id}"),
        InlineKeyboardButton("лайк", callback_data=f"cb_like_{item_id}"),
    )
    return markup