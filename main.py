import telebot
from currency_converter import CurrencyConverter
from telebot import types
bot = telebot.TeleBot('6344283762:AAF-irtJ70XnZn8y0o4LAzrW0z3kooQWzZs')

currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def main(message,):
    file = open('photo_2023-07-02_00-08-48.jpg', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть приложкение', url='https://vk.com'))
    bot.send_photo(message.chat.id, file, 'Добро пожаловать в магазин', reply_markup=markup)


@bot.message_handler(commands=['market'])
def market(message,):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Магазин🛒', callback_data='btn1')
    btn5 = types.InlineKeyboardButton('Корзина🗑', callback_data='btn5')
    btn2 = types.InlineKeyboardButton('Профиль👤', callback_data='btn2')
    btn3 = types.InlineKeyboardButton('FAQ❓', callback_data='btn3')
    btn4 = types.InlineKeyboardButton('Поддержка🙋‍♂️', callback_data='btn4')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton('Обувь', callback_data='обувь')
        btn2 = types.InlineKeyboardButton('Одежда', callback_data='одежда')
        btn3 = types.InlineKeyboardButton('Аксессуары', callback_data='аксессуары')
        btn4 = types.InlineKeyboardButton('Premium', callback_data='premium')
        btn5 = types.InlineKeyboardButton('Назад', callback_data='назад')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Каталог', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn5':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Магазин🛒', callback_data='btn1')
        btn5 = types.InlineKeyboardButton('Корзина🗑', callback_data='btn5')
        btn2 = types.InlineKeyboardButton('Профиль👤', callback_data='btn2')
        btn3 = types.InlineKeyboardButton('FAQ❓', callback_data='btn3')
        btn4 = types.InlineKeyboardButton('Поддержка🙋‍♂️', callback_data='btn4')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Каталог', reply_markup=markup)

bot.polling(none_stop=True)
