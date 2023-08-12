import telebot
from telebot import types
import requests
token = "6342888882:AAFEdS_IaZG8G6pUsSVzfDy0g5OU4kQqr-0"#توكنك
bot = telebot.TeleBot(token)

btn1 = types.InlineKeyboardButton(text = "مشاهدات تليكرام",callback_data="s1")

btn2 = types.InlineKeyboardButton(text = "مشاهدات تيك توك",callback_data="s2")

ch = types.InlineKeyboardButton(text= "قناتي", url = "https://t.me/astathon")

@bot.message_handler(commands=["start"])
def start(message):
	us = message.from_user.first_name
	b = types.InlineKeyboardMarkup()
	b.add(btn1,btn2)
	b.add(ch)
	bot.reply_to(message, text=f"""- اهلا {us} في بوت رشق مشاهدات 
& تحكم بلإزرار بلـ أسفل""",reply_markup=b)
	

@bot.callback_query_handler(func=lambda call:True)
def a(call):
        if call.data =="s1":
        	BROK(call.message)
        elif call.data == "s2":
        	brok(call.message)

def BROK(message):
		bot.send_message(message.chat.id, text = "ارسل الرابط لارشق المشاهدات")
		@bot.message_handler(func=lambda m:True)
		def vi(message):
			msg = message.text
			url = requests.get(f'https://smmabaza.shop/api/v2?action=add&service=827&link={msg}&quantity=1000&key=D4Qtf0zSEBhjmDlVOEQOFskE7U5lcaHl6XvCBVrQD2AVlBVA892VSntA4UUC').text
			bot.send_message(message.chat.id,url)
def brok(message):
		bot.send_message(message.chat.id, text = "ارسل الرابط لارشق المشاهدات")
		
		@bot.message_handler(func=lambda m:True)
		def vo(message):
				msg = message.text
				url = requests.get(f'https://smmabaza.shop/api/v2?action=add&service=824&link={msg}&quantity=1000&key=D4Qtf0zSEBhjmDlVOEQOFskE7U5lcaHl6XvCBVrQD2AVlBVA892VSntA4UUC').text
				bot.send_message(message.chat.id,url)

		
print('run')
bot.infinity_polling()

