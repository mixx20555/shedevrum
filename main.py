import telebot
from config import token
from logic import *
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет, я бот для генерации изображений. Отправь мне описание картинки, и я сгенерирую её для тебя.")

@bot.message_handler(func=lambda message: True)
def generate_image(message):
    prompt = message.text
    api = imgAPI()
    image_path = api.download_image(prompt)
    with open(image_path, 'rb') as file:
        bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, f"Генерирую изображение по описанию: {prompt}")

bot.infinity_polling()
    