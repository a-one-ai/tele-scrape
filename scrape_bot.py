import time
import telebot
import datetime
import os
import requests

BOT_TOKEN = '6876588658:AAGig2B_FJGF4KmwlhA_EOF8ldQA5SV2-e0'


bot = telebot.TeleBot(BOT_TOKEN)
bot_start_time = time.time()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_image(message):
    print(message)


@bot.message_handler(content_types=['photo'])
def download_image(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        chat_folder = f"chat_{message.chat.id}"
        if not os.path.exists(chat_folder):
            os.makedirs(chat_folder)

        current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{chat_folder}/{current_time}.jpg"
        
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        print(f"Image saved as {file_name}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    bot.infinity_polling()