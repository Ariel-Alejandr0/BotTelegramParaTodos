import telepot #modulo para criar e gerenciar um bot de telegram;
from time import sleep #serve para fazer pausas no programa;
from os import linesep #serve para dar quebra de linha;

#link de previsão do tempo que será enviado;
link = "https://www.google.com/search?q=previs%C3%A3o+do+tempo&oq=previs%C3%A3o+do&aqs=chrome.2.69i57j69i59l2j69i60l2.8463j0j1&sourceid=chrome&ie=UTF-8"

token = '***COLE_O_SEU_TOKEN_AQUI***'#token do bot;

bot = telepot.Bot(token) #passando o token para poder gerenciar o bot;

cont = 0 #contador, serve para impedir envio excessivo de mensagens;

mensagemEnviada = False # variável para verificar o envio da mensagem;

OldData = 0 # variável qua armazena  a antiga data;

while True: # Loop infinito para bot nunca parar.

    atualizacaoes = bot.getUpdates() #pega todas as informações do bot;
    
                                         #pega o ultimo elemento da variável
    EditAtualizacoes = atualizacaoes[-1] #neste caso serve apenas para simplificar,
                                         #a variável anterior;    
                  
    DATA = int(EditAtualizacoes['message']['date']) #pega o ID da mensagem;
    CHAT_ID = int(EditAtualizacoes['message']['chat']['id']) #pega o ID do chat;
    NOME = str(EditAtualizacoes['message']['from']['first_name']) # pega o nome de quem enviou a msg; 
    PegarMensagens = str(EditAtualizacoes['message']['text']) #pega a mensagem enviada;

    if DATA != OldData: # verifica se existe diferença entre as atualizações de msg; 
        mensagemEnviada = False # Mensagem ainda não foi envida;

    OldData = DATA

    if mensagemEnviada == False: #se mensagem não foi enviada; 
        if PegarMensagens == "/tempo": #verifica se a mensagem é igual a /tempo;
            bot.sendMessage(CHAT_ID,f'Olá {NOME} aqui está o link: {linesep}{link}') #envia o link para o seguinte chat ID;
            print(PegarMensagens)
            print(NOME)
            mensagemEnviada = True # mensagem foi enviada;

    sleep(0.1) #pausa de 1 segundo;
