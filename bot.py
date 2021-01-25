import telepot #modulo para criar e gerenciar um bot de telegram;
from time import sleep #serve para fazer pausas no programa;
from os import linesep #serve para dar quebra de linha;

#link de previsão do tempo que será enviado;
link = "https://www.google.com/search?q=previs%C3%A3o+do+tempo&oq=previs%C3%A3o+do&aqs=chrome.2.69i57j69i59l2j69i60l2.8463j0j1&sourceid=chrome&ie=UTF-8"

token = '1572619085:AAEgPMqcm0MXOzQIBWo7z7EGEIyE_f_Iu8s'#token do bot;

bot = telepot.Bot(token) #passando o token para poder gerenciar o bot;

cont = 0 #contador, serve para impedir envio excessivo de mensagens;

mensagemEnviada = False # variável para verificar o envio da mensagem;



old_data = 0 # variável qua armazena  a antiga data;

print("iniciou!!!")

while True: # Loop infinito para bot nunca parar.

    atualizacaoes = bot.getUpdates() #pega todas as informações do bot;
    
                                         #pega o ultimo elemento da variável
    EditAtualizacoes = atualizacaoes[-1] #neste caso serve apenas para simplificar,
                                         #a variável anterior;
    
    class Dados: # classe DADOS
        def __init__(self, msg, IS_texto): # função que cria todas as características da classe
            self.data = int(EditAtualizacoes[msg]['date']) #pega o ID da mensagem;
            
            self.chat_id = int(EditAtualizacoes[msg]['chat']['id']) #pega o ID do chat;
            self.nome = str(EditAtualizacoes[msg]['from']['first_name']) # pega o nome de quem enviou a msg; 
            self.PegarMensagens = str(EditAtualizacoes[msg][IS_texto]) #pega a mensagem enviada;

    try:
        dadosFormatados = Dados('message', 'text') # dadosFormatados recebe a classe DADOS sendo que o parametro msg se torna 'message';
    
    except(KeyError): # tratamento de exceção
        dadosFormatados = Dados('message', 'sticker') # caso uma mensagem sofra uma edição e cause um KeyError,
                                         # o parametro msg deixa de ser 'message' e se torna 'edited_message';
    except(KeyError):
        dadosFormatados = Dados('edited_message', 'text')
    
    except(KeyError):
        dadosFormatados = Dados('edited_message', 'sticker')

    if dadosFormatados.data != old_data: # verifica se existe diferença entre as atualizações de msg; 
        mensagemEnviada = False # Mensagem ainda não foi envida;
    else:
        mensagemEnviada = True
    old_data = dadosFormatados.data

    if mensagemEnviada == False: #se mensagem não foi enviada; 
        if dadosFormatados.PegarMensagens == "/tempo": #verifica se a mensagem é igual a /tempo;
            bot.sendMessage(dadosFormatados.chat_id,f'Olá {dadosFormatados.nome} aqui está o link: {linesep}{link}') #envia o link para o seguinte chat ID;
            print(dadosFormatados.PegarMensagens) # ecreve no meu terminal /tempo
            print(dadosFormatados.nome) # mostra o nome do infeliz que enviou a mensagem;
            mensagemEnviada = True # mensagem foi enviada;

    sleep(0.1) #pausa de 1 segundo;
