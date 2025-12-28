from telebot import TeleBot, types
from parser import parse
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='token.env')

TOKEN = os.getenv('TOKEN')
bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🔍 Detective")
    btn2 = types.KeyboardButton("🔥 Action")
    btn3 = types.KeyboardButton("🎬 Trailer")
    btn4 = types.KeyboardButton("🧟‍♀️ Horror")
    btn5 = types.KeyboardButton("➕ More")

    keyboard.add(btn1, btn2, btn3)
    keyboard.add(btn4, btn5)

    bot.send_message(
        message.chat.id,
        'Բարև բարի գալուստ ֆիլմերի որոնման բոտ 😊\nԸնտրեք ժանրը․',
        reply_markup=keyboard
    )

    bot.send_photo(message.chat.id, open('image.jpg', 'rb'))

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    text = message.text

    if text == "🔍 Detective":
        bot.send_message(message.chat.id, "Լավ, ցուցադրում եմ դետեկտիվ ֆիլմերը…")
        data = parse('mystery')
        bot.send_message(message.chat.id, data)

    elif text == "🔥 Action":
        bot.send_message(message.chat.id, "Ահա գործողություններով լի ֆիլմերը…")

    elif text == "🎬 Trailer":
        bot.send_message(message.chat.id, "Նայեք ամենաթարմ թրեյլերները…")

    elif text == "🧟‍♀️ Horror":
        bot.send_message(message.chat.id, "Նայեք ամենաթարմ թրեյլերները…")
        data = parse('horror')
        bot.send_message(message.chat.id, data)

    elif text == "➕ More":
        bot.send_message(message.chat.id, "Շարունակում եմ ավելացնել նոր ֆունկցիաներ…")

    else:
        bot.send_message(message.chat.id, "Խնդրում եմ ընտրեք կոճակներից որևէ մեկը։")


bot.polling(none_stop=True)