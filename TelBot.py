import telebot
import NBU

bot = telebot.TeleBot("*****")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Текущий курс валют НБУ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def answer_message(message):
    if message.text == 'Привет':
        bot.send_sticker(message.chat.id, 'CAADAgADVwADJDhNDB4ceiscASFmFgQ')
    elif message.text == 'Текущий курс валют НБУ':
        objNbu = NBU.Nbu()
        bot.send_message(message.chat.id, objNbu.today_currencies())
    else:
        bot.send_message(message.chat.id, 'Тебе здесь не рады, уходи или пиши /start.')

# for getting sticker id
# @bot.message_handler(content_types=['sticker'])
# def get_sticker_id(message):
# 	print(message)

bot.polling()
