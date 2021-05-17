# coding=utf-8
import telebot
import random
import const
import smtplib



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
    key.row('Оставить заявку')
    key.row('Популярные вопросы')
    key.row('О нас', 'Контакты')
    bot.send_message(message.chat.id, 'Привет я бот-помошник WorkAsistPoland, чем могу помочь?', reply_markup=key)


@bot.message_handler(content_types=['text', 'contact'])
def main(message):
    global keks
    keks = 'keks'
    if message.text == 'О нас':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_message(message.chat.id, 'Work Asist Poland - это команда профессионалов с многолетним опытом в сфере трудоустройства.\n\nМы оказываем высококачественные комплексные услуги в сфере трудоустройства :\n\n- Предоставляем помощь в открытии визы ,подбора вакансии ;\n\n- Предоставляем официальное трудоустройство , подписываем договор (Umowa Zlecenia), оплачиваем налоги/страховку;\n\n- Обеспечиваем жильем и необходимой поддержкой каждого нашего работника 24/7;\n\n- Предоставляем комфортные условия труда и высокую оплату ;\n\nWork Asist Poland ежедневно усердно работает и развивается  ради Вас , чтобы приехав в первые , вы чувствовали себя максимально комфортно и безопасно , мы создаем лучшие условия труда и проживания .Ведь каждый из нашей команды проходил этот неизведанный путь в чужой стране и мы как никто другой знаем важность и силу поддержки .Не смотря на сложность всей  ситуации в связи с пандемией в мире , Work Asist не на минуту не прекратили работу , а наоборот благодаря сплоченности нашей команды в условиях карантина мы обеспечили новые рабочие места , организовали трансферы для прибытия кандидатов с Украины в Польшу и предоставляем жилье на время обсервации .Мы всегда на связи и готовы прийти на помощь .У нас есть вакансии для всех и каждого .\n\n📌Если вы в поисках работы в Польше -мы готовы Вам помочь🤝С радостью ответим на все интересующие Вас вопросы по телефону , в социальных сетях или же при личной встрече в одном из наших офисов в Польше или в Украине .🇵🇱🇺🇦')
        send = bot.send_message(message.chat.id, 'Нажмите "Ⓜ Главное меню", если хотите венуться в главное меню ⤵', reply_markup=keyboard)
        bot.register_next_step_handler(send, main)
    elif message.text == 'Оставить заявку':
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        msg = bot.send_message(message.chat.id, 'Напишите боту следующие данные а наш специалист с вами свяжется.Пример заявки для обратной связи:\n\n1.ФИО\n\n2.Возраст\n\n3.Контактный телефон\n\n 4.Текущее местоположение.\nДля корректно сформированной заявки следует отправить все данные  ОДНИМ целым сообщением')
        bot.register_next_step_handler(msg,sending)
        bot.send_message(message.chat.id, 'Нажмите "Ⓜ Главное меню", если хотите венуться в главное меню ⤵', reply_markup=keyboard)
    elif message.text == 'Популярные вопросы':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_message(message.chat.id, "1) Как добраться к офису на оформление ?✅✅✅\n\n Наши офисы расположены близко к ж/д и автовокзалу, поэтому Вы без труда к нам доберетесь. В случае возникновения каких-либо проблем, с Вами на связи будет наш специалист Отдела Сопровождения, который в телефонном режиме ответит на все Ваши вопросы и поможет в решении каких-либо проблем. Постоянно будет находиться с Вами в контакте, поэтому если Ваш приезд планируется после 16:00 – мы забронируем для Вас место в хостеле. И в телефонном режиме сопроводим Вас до места. Также предоставим маршрутный лист с адресом нашего офиса.\n\n"),
        bot.send_message(message.chat.id,"2)  Можно ли резервировать места на вакансию ?✅✅✅\n\n- К сожалению такого понятия как резервирование вакансии нет. Но лучшим решением будет открыть визу на вакансию которая вам понравилась,таким образом среди других желающих вы становитесь приоритетным и в первую очередь по актуализации вакансии мы свяжемся с вами.\n\n"),
        bot.send_message(message.chat.id,"3) Есть ли проезд с проживания до места работы?✅✅✅\n\nЕсли речь идет о проезде с мест проживание которые мы предоставляем до места работы и обратно ,то проездом обеспечиваем.Исключением являются случаи в которых проживание находится в пешей доступности.Если же вы проживаете на своем жилье в таком случае проезд не предоставляем\n\n"),
        bot.send_message(message.chat.id,"4) Обязательно ли проходить обсервацию или можно сдать тест ?✅✅✅\n\nСогласно изменениям, с 30.03 все приезжающие попадают на обязательную обсервацию.Тест на COVID – 19 сдаётся на территории Польши по приезду. Предварительная стоимость от 150 злотых. Кандидаты оплачивают самостоятельно.На время прохождения теста и ожидания результата - жильё предоставляется бесплатно!При наличии позитивного теста жильё на время обсервации предоставляется, кандидаты оплачивают его самостоятельно.\n\nСтоимость (в зависимости от города приезда) 300 – 350зл.\nЕсли кандидаты не желают сдавать тест, а проходить обсервацию, то оплачивают самостоятельно!"),
        bot.send_message(message.chat.id, "5) Условия проживания ?✅✅✅\n\nУсловия проживания у нас стандартные. Есть wi-fi, несколько санузлов, стиральные машины и т.п. В комнате проживают от 2 до 4 человек. Семейные пары селим отдельно или вместе с другой семейной парой ,во втором случае работают в разные смены. Есть отдельные комнаты для женщин и мужчин. Суммы за проживание высчитываются из заработной платы, сумма варьируется от 250 до 350 зл/мес. За свое проживание есть компенсация в ЗП."),
        bot.send_message(message.chat.id, "6) Официально ли трудоустройство ?✅✅✅\n\nДа ,наше трудоустройство полностью официальное !Мы оплачиваем вам страховку и налоги.\n\n"),
        bot.send_message(message.chat.id, "7) Граждан каких стран трудоустраиваете?✅✅✅\n\nНаше агентство трудоустраивает граждан шести стран :\n- Украина \n- Россия\n- Беларусь \n- Молдова \n- Грузия\n- Армения\n\n"),
        bot.send_message(message.chat.id, "8)Hoмep PESEL в Пoльшe — кaк пoлyчить инocтpaнцy?✅✅✅\n\nBce ктo пpиeзжaeт жить в Пoльшy, paнo или пoзднo, cтoлкнyтcя c тeм, чтo нeкoтopым гocyдapcтвeнным и чacтным opгaнизaциям нyжнo пpeдocтaвить нoмep PESEL.\nPESEL - этo yникaльный идeнтификaтop или нoмep нaлoгoплaтeльщикa.\nЛюбыe cepьeзныe oпepaции, тaкиe кaк oткpытиe cчeтa в бaнкe, peгиcтpaция aвтoмoбиля или дaжe вызoв Cкopoй Пoмoщи тpeбyют пpeдocтaвлeния личнoгo нoмepa PESEL. He гoвopя yжe пpo пoпыткy взять кpeдит в бaнкe или пoкyпкy нeдвижимocти.\nKaк пoлyчить PESEL в Пoльшe?Для пoлyчeния PESEL нe нyжнo coбиpaть кyчy дoкyмeнтoв, дocтaтoчнo лишь нecкoлькиx.Ocнoвным ycлoвиeм пoлyчeния нoмepa PESEL являeтcя oфopмлeниe вpeмeннoй или пocтoяннoй пpoпиcки - zameldowanie нa тeppитopии Пoльши. Для этого вам  нeoбxoдимo имeть дeйcтвитeльнyю визy (биометрию) или Kapтy Пoбытa и дoгoвop apeнды жилья.Пocлe peгиcтpaции, нyжнo лишь пoдaть зaявкy, чтo вы xoтитe пoлyчить cпpaвкy co cвoим нoмepoм PESEL.Bтopoй нeoбxoдимый дoкyмeнт — yдocтoвepeниe личнocти. Peчь идeт o зaгpaнпacпopтe c визoй или кapтoй пoбытy, ecли oнa имeeтcя.Hижe oпиcaнa пocлeдoвaтeльнocть дeйcтвий, кoтopыe нyжнo выпoлнить в Ужoндe (Urzad) чтoбы пoлyчить PESEL:\n1. Hyжнo зapeгиcтpиpoвaтьcя в элeктpoннoй cиcтeмe или по телефону;\n2. Идeтe в yжoнд, гдe вас пропишут (сделают мeльдунек);\n3.	Бepeтe c coбoй пacпopт и договор найма жилья;\n4. Зaпoлняeтe aнкeтy для прописки   Zgłoszenie pobytu czasowego, на основании которой вам сделают PESEL.\nBce, в peзyльтaтe y вac нa pyкax ocтaeтcя блaнк c пeчaтями и пoдпиcями, гдe yкaзaн вaш нoмep PESEL.\nBce oфopмлeния зaнимaют нecкoлькo минyт."),
        bot.send_message(message.chat.id, "9)Стоимость документов для выезда в Польшу ?:✅✅✅\n\n1.Стоимость освядчения ( приглашения 90/180)\n50 zł  или в грн по курсу НБУ компенсируем в первую ЗП по отработке месяца.\n\n2. Стоимость зезволения ( воевуда 365)\n600 zł для нового кандидата из них  -300 zł компннсируем в первую ЗП по тработке месяца.Если работник уже работает на нашей вакансии-300 zł .\n\n3.Стоимость услуг на получение визы 180 дней -1200 грн;\nВ пакет услуг входит: заполнение визового формуляра онлайн и всех требующихся бланков , страховка на 180 дней.\n\n4. Стоимость услуг в получении визы на 365 дней-1200 грн;\nВ пакет услуг входит: заполнение визового формуляра онлайн и всех требующихся бланков , страховка на 365 дней.\n\n5. Стоимость полного пакета документов под визу 180 дней-1600 грн;\n\nВ пакет услуг входит: приглашение на 180 дней, заполнение визового формуляра онлайн и всех требующихся бланков , страховка на 180 дней.\n\n")
        bot.send_message(message.chat.id, "10) Какие документы нужны для пересечения границы?✅✅✅\n\n -приглашение (виза/био/зазволение);\n-адрес прохождения карантина;\n-страховка.")
        bot.send_message(message.chat.id, 'Нажмите "Ⓜ Главное меню", если хотите венуться в главное меню ⤵', reply_markup=keyboard)
    elif message.text == 'Контакты':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_message(message.chat.id, 'Instagram: https://instagram.com/workasistpoland?igshid=p4mkd711363q \nНаш сайт: https://www.workasistpoland.com.pl  \nTelegram канал с вакансиями: t.me/workasistpoland \n Рекрутор Дарья: +48 533 653 410 \n Рекрутор Анастасия: +48 570 628 574 \n Рекрутор Елена: +48 535 224 531\n\nНаши офисы: \n\nPoznań,\nul. Taczaka 24,\n61-819\nTel.: +(48) 533-641-064\n\nŁódź\nul. Zachodnia 70\n90-411\nTel.: +(48) 533-052-246 \n\nKatowice\nul. Mickiewicza 10/102\n40-092\nTel.: +(48) 533-641-064', reply_markup=keyboard)
    elif message.text == 'Ⓜ Главное меню':
        first(message)

def sending(message):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('wap.bot.mail', 'Test.,123Bot')
    smtpObj.sendmail("wap.bot.mail@gmail.com", "o.kondel@workasistpoland.com.pl", message.text.encode("utf8"))
    smtpObj.quit()

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