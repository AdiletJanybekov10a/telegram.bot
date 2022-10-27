import telebot
from googletrans import Translator

TOKEN = '...'

bot = telebot.TeleBot(TOKEN)
translator = Translator()

@bot.message_handler(commands=['start'])
def message_start(message) :
    bot.reply_to(message , 'Привет я бот переводчик')
    bot.send_message(message.chat.id, '<strong>Введите слово для перевода</strong>', parse_mode='html' )
    
@bot.message_handler()
def message_translate(message) :
    print(translator.translate(message.text, dest='ru').text)
    if message.text == translator.translate(message.text, dest='ru').text :
     bot.reply_to(message , translator.translate(message.text , dest='en').text)
    else :
     bot.reply_to(message , translator.translate(message.text , dest='ru').text)

bot.infinity_polling()