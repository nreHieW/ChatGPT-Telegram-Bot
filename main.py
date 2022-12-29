from revChatGPT.ChatGPT import Chatbot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time
import os
import json

with open('config.json') as f:
  data = json.load(f)
  token = data.get('session_token')
  API_KEY = data.get('API_Key')

def send_request(input_text):
  return chatbot.ask(input_text)['message']


def start(update: Update, context: CallbackContext):
  update.message.reply_text(send_request(update.message.text))


def handle_message(update: Update, context: CallbackContext):
  text = update.message.text
  update.message.reply_text(send_request(text))


if __name__ == '__main__':
  #initialisation
  try_count = 0
  chatbot = Chatbot({"session_token":token}, conversation_id=None, parent_id=None) 
  while chatbot.config.get('Authorization') == None:
    time.sleep(2)
    try_count +=1
    if try_count == 20:
      quit()
      

  updater = Updater(API_KEY, use_context=True)

  updater.dispatcher.add_handler(CommandHandler('start', start))
  updater.dispatcher.add_handler(
    MessageHandler(filters=Filters.text, callback=handle_message))
  updater.start_polling()
  updater.idle()
