import telepot #modulo para criar e gerenciar um bot de telegram;
from time import sleep #serve para fazer pausas no programa;
from os import linesep #serve para dar quebra de linha;

#link de previsão do tempo que será enviado;
link = "https://www.google.com/search?q=previs%C3%A3o+do+tempo&oq=previs%C3%A3o+do&aqs=chrome.2.69i57j69i59l2j69i60l2.8463j0j1&sourceid=chrome&ie=UTF-8"

token = 'COLOQUE_SEU_TOKEN_AQUI'#token do bot;

bot = telepot.Bot(token) #passando o token para poder gerenciar o bot;

mensagemEnviada = False # variável para verificar o envio da mensagem;

OldData = 0 # variável qua armazena  a antiga data;

while True: # Loop infinito para bot nunca parar.

    atualizacaoes = bot.getUpdates() #pega todas as informações do bot;
    
                                         #pega o ultimo elemento da variável
    EditAtualizacoes = atualizacaoes[-1] #neste caso serve apenas para simplificar,
                                         #a variável anterior;
    
    class DADOS: # classe DADOS
        def __init__(self, msg): # função que cria todas as características da classe
            self.DATA = int(EditAtualizacoes[msg]['date']) #pega o ID da mensagem;
            
            self.CHAT_ID = int(EditAtualizacoes[msg]['chat']['id']) #pega o ID do chat;
            self.NOME = str(EditAtualizacoes[msg]['from']['first_name']) # pega o nome de quem enviou a msg; 
            self.PegarMensagens = str(EditAtualizacoes[msg]['text']) #pega a mensagem enviada;

    try:
        DADOS1 = DADOS('message') # DADOS1 recebe a classe DADOS sendo que o parametro msg se torna 'message';
    
    except(KeyError): # tratamento de exceção
        DADOS1 = DADOS('edited_message') # caso uma mensagem sofra uma edição e cause um KeyError,
                                         # o parametro msg deixa de ser 'message' e se torna 'edited_message';


    if DADOS1.DATA != OldData: # verifica se existe diferença entre as atualizações de msg; 
        mensagemEnviada = False # Mensagem ainda não foi envida;

    OldData = DADOS1.DATA

    if mensagemEnviada == False: #se mensagem não foi enviada; 
        if DADOS1.PegarMensagens == "/tempo": #verifica se a mensagem é igual a /tempo;
            bot.sendMessage(DADOS1.CHAT_ID,f'Olá {DADOS1.NOME} aqui está o link: {linesep}{link}') #envia o link para o seguinte chat ID;
            print(DADOS1.PegarMensagens) # ecreve no meu terminal /tempo
            print(DADOS1.NOME) # mostra o nome do infeliz que enviou a mensagem;
            mensagemEnviada = True # mensagem foi enviada;

    sleep(0.1) #pausa de 1 segundo;
