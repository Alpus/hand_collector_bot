import os
from io import BytesIO
from urllib import request

import telebot
import uuid
from PIL import Image

import settings
from settings import messages, paths


bot = telebot.TeleBot(settings.private.API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages.HELP_MESSAGE)


@bot.message_handler(content_types=['document'])
def handle_doc(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        file_url = 'https://api.telegram.org/file/bot{}/{}'.format(
            settings.private.API_TOKEN,
            file_info.file_path,
        )
        img = request.urlopen(file_url).read()

        img_for_check = Image.open(BytesIO(img))
        img_for_check.verify()

        file_path = os.path.join(paths.IMAGES_DIR, str(uuid.uuid4()) + '.png')
        with open(file_path, 'wb') as file:
            file.write(img)

        bot.send_message(message.chat.id, messages.THANKS_MESSAGE)
    except:
        bot.send_message(message.chat.id, messages.BAD_IMAGE_MESSAGE)


@bot.message_handler(content_types=['photo', 'audio', 'video'])
def handle_doc(message):
    bot.send_message(message.chat.id, messages.NO_PHOTO_MESSAGE)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, messages.NO_PHOTO_MESSAGE)


if __name__ == '__main__':
    bot.polling()
