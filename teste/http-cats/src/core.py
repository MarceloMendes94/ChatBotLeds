from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL

def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_CATS_URL + args[0]
    )


def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def summarize(bot, update):
    try:
        # Get the text the user sent
        text = update.message.text
        print(text)
        # Run it through the summarizer
        #summary = algo.pipe(text)
        # Send back the result
        bot.sendMessage(chat_id=update.message.chat_id, 
        text="oi")
    except UnicodeEncodeError:
        bot.sendMessage(chat_id=update.message.chat_id, 
        text="Sorry, but I can't summarise your text.")


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(  CommandHandler('start', start)                     )
    dispatcher.add_handler(  CommandHandler('http', http_cats, pass_args=True)  )
    #dispatcher.add_handler(  MessageHandler(Filters.text, echo))
    summarize_handler = MessageHandler([Filters.text], summarize)
    dispatcher.add_handler(summarize_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()