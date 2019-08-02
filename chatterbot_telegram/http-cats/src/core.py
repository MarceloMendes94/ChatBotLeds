# bibliotecas para telegram
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
#-------------------------------------------------------------------------

#bibliotecas para chatterbot
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer




#-------------------------------------------------------------------------

#funções telegram --------------------------------------------------------
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

def chat_telegram(bot, update):   
    try:
        chatbot = ChatBot('Charlie')
        trainer = ListTrainer(chatbot)
        trainer.train([     "oi",    "oi, tudo bem?",    "ei",    "oi, tudo bem?"])
        # Get the text the user sent
        text = update.message.text
        chatbot = ChatBot("Charlie")
        print(type(chatbot))
        response = chatbot.get_response(text)
        bot.sendMessage(chat_id=update.message.chat_id, 
        text=response.text)
    except UnicodeEncodeError:
        bot.sendMessage(chat_id=update.message.chat_id, 
        text="Sorry, but I can't summarise your text.")


def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(  CommandHandler('start', start)                     )
    dispatcher.add_handler(  CommandHandler('http', http_cats, pass_args=True)  )
    summarize_handler = MessageHandler(Filters.text, chat_telegram)
    dispatcher.add_handler(summarize_handler)



    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    # -prompt-chat -voice-chat --help -telegram-chat
    if(len(sys.argv)== 1):
        print("--help  to be helped")
    else:
        if(sys.argv[1]=="--help"):
            print("-telegram-chat chat via telegram")
        elif(sys.argv[1]=="-voice-chat"):
            print("chat via voz")
        elif(sys.argv[1]=="-prompt-chat"):
            print("chat via terminal")
            #chat_prompt()
        elif(sys.argv[1]=="-telegram-chat"):
            print("Abra o telegram @andreangelobot press CTRL + C to cancel.")
            main()   
        else:
            print("--help  to be helped")