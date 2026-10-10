import os
import telebot
from flask import Flask
from threading import Thread
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "البوت شغال 24 ساعة")
@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, m.text)
app = Flask('')
@app.route('/')
def home():
    return "alive"
Thread(target=lambda: app.run(host='0.0.0.0', port=10000)).start()
bot.infinity_polling()
