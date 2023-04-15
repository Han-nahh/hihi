from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from fastapi import FastAPI
import os

TOKEN = os.environ.get("TOKEN")


app=FastAPI()
@app.get("/")
def index():
    return {"message": "Hello World"}
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def register_handlers(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

def main():
    updater = Updater(token='5998043260:AAFOmDM1F1JXNmfOvC2azwk7sweb-w4bX3k', use_context=True)
    dispatcher = updater.dispatcher

    register_handlers(dispatcher)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()