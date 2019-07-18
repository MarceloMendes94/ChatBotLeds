#-*- coding: utf-8 -*-
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
    
def main():
    # -prompt-chat -voice-chat --help -telegram-chat
    if(len(sys.argv)== 1):
        print("--help  to be helped")
    else:
        if(sys.argv[1]=="--help"):
            print("-prompt-chat  chat via termianl.\n-voice-chat  chat via voz.\n")
        elif(sys.argv[1]=="-voice-chat"):
            print("chat via voz")
        elif(sys.argv[1]=="-prompt-chat"):
            print("chat via terminal")
            chat()
        else:
            print("--help  to be helped")
#fim main 
   
def chat():
    #criando chat
    chatbot = ChatBot("Ron Obvious")
    #lista de conversas
    arquivo = open('../conversas.txt','r')
    linha=arquivo.readline()
    linha=linha[:-1]
    i=0
    lista=[]
    while len(linha)!=0:
        lista.append(linha)
        linha=arquivo.readline()    
        linha=linha[:-1]
        i=i+1
    #treinando
    trainer = ListTrainer(chatbot)
    trainer.train(lista)
    trainer.train(lista)
    trainer.train(lista)
    #conversa
    you=input('voce: ')
    while 'tchau' not in you:
        response = chatbot.get_response(str(you))
        print('bot:',response)
        you=input('voce: ')
    #fim while
    print('tchau até breve!')
#fim chat

if __name__== "__main__":
    main()