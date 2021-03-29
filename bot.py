# coding=utf-8
import telebot
import random
import const


from telebot import types

TOKEN = '1744573399:AAHMtT4PGpa6RneERz7k_fnTiY-92YSpagk'
PHOTO_RIK = 'AgACAgQAAxkBAAIDZV-l2fZ3Rt3OHBn7RiuH5Ch7S4kxAAImtTEblogxUTfvieIOyOhQRDDcJ10AAwEAAwIAA20AA5UIAgABHgQ'
PHOTO_Z1 = 'AgACAgQAAxkBAAIDbl-l20iW5BZj9Z5vZlxqUzeazl0oAAIntTEblogxUY2pfA0Dw5naOPseJ10AAwEAAwIAA20AA434AQABHgQ'
PHOTO_Z2 = 'AgACAgQAAxkBAAIDb1-l231WjVbXI3rfryDwFZNJ9zUlAAIstTEblogxURhJcSqHnl6zTPAbJ10AAwEAAwIAA20AA97zAQABHgQ'
PHOTO_otz = 'AgACAgQAAxkBAAIGtF-oaqFsb7E5bLn8r5DVki9VKgZCAAIZtDEbOZxJUQ1O8fRvgexBtnHrJ10AAwEAAwIAA20AA1z4AQABHgQ'

bot = telebot.TeleBot(const.TOKEN)

@bot.message_handler(commands = ['start'])
def first(message):
    key = types.ReplyKeyboardMarkup(True, True)
    key.row('Товары')
    key.row('Отзывы')
    key.row('О нас', 'Контакты')
    bot.send_message(message.chat.id, 'Привет я бот-помошник WorkAsistPoland, чем могу помочь?', reply_markup=key)


@bot.message_handler(content_types=['text', 'contact'])
def main(message):
    global keks
    keks = 'keks'
    if message.text == 'О нас':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_message(message.chat.id, 'Мы являемся агентством по трудоустройству, которое более 10 лет активно работает на польском рынке.✅✅✅ \n\nМы предлагаем комплексные услуги в области аутсорсинга персонала и временной занятости, которые мы всегда предоставляем на самом высоком уровне.✅✅✅ \n\nНаша команда опытных специалистов постоянно занимается поиском работников с Востока, реагируя на потребности рынка труда, поэтому мы можем удовлетворить высокие требования каждого Клиента независимо от отрасли.✅✅✅')
        send = bot.send_message(message.chat.id, 'Нажмите "Ⓜ Главное меню", если хотите венуться в главное меню ⤵', reply_markup=keyboard)
        bot.register_next_step_handler(send, main)
    elif message.text == 'Товары':
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        stik1 = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='25шт-100 грн', callback_data='butt1')
        but_2 = types.InlineKeyboardButton(text='50шт-200 грн', callback_data='stik1')
        but_3 = types.InlineKeyboardButton(text='100шт-300 грн', callback_data='stik1')
        stik1.add(but_1)
        stik1.add(but_2)
        stik1.add(but_3)
        keyboard.row('Ⓜ Главное меню')
        # bot.send_photo(message.chat.id, PHOTO_RIK, caption='Стикер пак №1', reply_markup=stik1)
        stik2 = types.InlineKeyboardMarkup()
        but_4 = types.InlineKeyboardButton(text='25шт-100 грн', callback_data='stik2')
        but_5 = types.InlineKeyboardButton(text='50шт-200 грн', callback_data='stik2')
        but_6 = types.InlineKeyboardButton(text='100шт-300 грн', callback_data='stik2')
        stik2.add(but_4)
        stik2.add(but_5)
        stik2.add(but_6)
        # bot.send_photo(message.chat.id, PHOTO_Z1, caption='Стикер пак №2', reply_markup=stik2)
        stik3 = types.InlineKeyboardMarkup()
        but_7 = types.InlineKeyboardButton(text='25шт-100 грн', callback_data='stik3')
        but_8 = types.InlineKeyboardButton(text='50шт-200 грн', callback_data='stik3')
        but_9 = types.InlineKeyboardButton(text='100шт-300 грн', callback_data='stik3')
        stik3.add(but_7)
        stik3.add(but_8)
        stik3.add(but_9)
        # bot.send_photo(message.chat.id, PHOTO_Z2, caption='Стикер пак №3', reply_markup=stik3)
        bot.send_message(message.chat.id, 'Нажмите "Ⓜ Главное меню", если хотите венуться в главное меню ⤵', reply_markup=keyboard)
    elif message.text == 'Отзывы':
          sel = types.InlineKeyboardMarkup()
          but_10 = types.InlineKeyboardButton(text='Отзывы', url='https://t.me/joinchat/AAAAAFjvZ_zfsO4u5zRhIA', callback_data='sel')
          sel.add(but_10)
          # bot.send_photo(message.chat.id, PHOTO_otz, reply_markup=sel)
          if message.text == 'Отзывы':
           keyboard = types.ReplyKeyboardMarkup(True, False)
           keyboard.row('Ⓜ Главное меню')
           bot.send_message(message.chat.id, 'Нажмите "Ⓜ Главное меню", если хотите венуться в главное меню ⤵', reply_markup=keyboard)
    elif message.text == 'Контакты':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_message(message.chat.id, 'Instagram: ********* \nTelegram канал с вакансиями: t.me/workasistpoland \n Рекрутор Дарья: +48 533 653 410 \n Рекрутор Анастасия: +48 570 628 574 \n Рекрутор Елена: +48 535 224 531\n\nНаши офисы: \n\nPoznań,\nul. Taczaka 24,\n61-819\nTel.: +(48) 533-641-064\n\nŁódź\nul. Zachodnia 70\n90-411\nTel.: +(48) 533-052-246 \n\nKatowice\nul. Mickiewicza 10/102\n40-092\nTel.: +(48) 533-641-064', reply_markup=keyboard)
    elif message.text == 'Ⓜ Главное меню':
        first(message)


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'butt1':
        key = types.ReplyKeyboardMarkup(True, False)
        key.row('Ⓜ Главное меню')
        send = bot.send_message(call.message.chat.id, 'Введите своё ФИО:', reply_markup=key)
        bot.register_next_step_handler(send, name)


def name(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
         keyboard = types.ReplyKeyboardMarkup(True, False)
         keyboard.row('Ⓜ Главное меню')
         send = bot.send_message(message.chat.id, 'Очень приятно, {name}. Оставьте, пожалуйста, Ваш номер телефона:'.format(name=message.text), reply_markup=keyboard)
         bot.register_next_step_handler(send, gorod)

def gorod(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Напишите город и отделение Новой Почты, для отправки товара:', reply_markup=keyboard)
        bot.register_next_step_handler(send, oplata)

def oplata(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_message(message.chat.id, 'Напишите город и отделение Новой Почты, для отправки товара:\n Номер вашего заказа: {}'.format(random.randint(1000, 9999)), reply_markup=keyboard)



bot.polling()