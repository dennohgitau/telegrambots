import constants as keys
from telegram.ext import *
import responses as r

print("I am alive")


def start(update, context):
    update.message.reply_text('Type something Random To get started')


def help(update, context):
    update.message.reply_text('If you need some help check the internet')


def handleMessage(update, context):
    text = str(update.message.text).lower()

    response = r.sampleResponses(text)

    update.message.replyText(response)


def error(update, context):
    print (f"Update {update} cause error {context.error}")


def main():
    updater = Updater(keys.API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))


    dp.add_handler(MessageHandler(Filters.text, handleMessage))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()



