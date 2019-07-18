# Biblioteca chatterbot python3
# Documentação
[link](https://chatterbot.readthedocs.io/en/stable/)

#Script
Rodando o script shell.sh vc pode instanciar no seu terminal uma VM python com a biblioteca e suas dependencias.
```
    indisponivel no momento
```
caso tenha problemas 
pode ser feito de forma manual abra um terminal na pasta chatterbot dentro desse repositório.
```
    sudo apt-get update
    sudo apt-get install virtualenv
    mkdir chatterbot-VM
    cd  chatterbot-VM
    virtualenv chatterbot
    source chatterbot/bin/activate
    clear
    pip3 install chatterbot
    pip3 install chatterbot-corpus
    cd ..
    cp chat.py chatterbot-VM/
    cd  chatterbot-VM
    python3 chat.py
```