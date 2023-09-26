import telepot #modulo para criar e gerenciar um bot de telegram;
from time import sleep #serve para fazer pausas no programa;
from os import linesep #serve para dar quebra de linha;

#link de previsão do tempo que será enviado;
link = "https://www.google.com/search?q=previs%C3%A3o+do+tempo&oq=previs%C3%A3o+do&aqs=chrome.2.69i57j69i59l2j69i60l2.8463j0j1&sourceid=chrome&ie=UTF-8"

link2 = "http://www.blumob.com.br/tabela-horarios"

token = 'COLE O SEU TOKEN AQUI'#token do bot;

bot = telepot.Bot(token) #passando o token para poder gerenciar o bot;

cont = 0 #contador, serve para impedir envio excessivo de mensagens;

mensagemEnviada = False # variável para verificar o envio da mensagem;

old_data = 0 # variável qua armazena  a antiga data;

print("iniciou!!!")

class Dados: # classe DADOS
        def __init__(self, msg, IS_texto): # função que cria todas as características da classe
            self.data = int(EditAtualizacoes[msg]['date']) #pega o ID da mensagem;
            
            self.chat_id = int(EditAtualizacoes[msg]['chat']['id']) #pega o ID do chat;
            self.nome = str(EditAtualizacoes[msg]['from']['first_name']) # pega o nome de quem enviou a msg; 
            self.PegarMensagens = str(EditAtualizacoes[msg][IS_texto]) #pega a mensagem enviada;
        
        
        def enviarMensagens(self):
            if self.PegarMensagens == '/tempo':
                bot.sendMessage(self.chat_id,f'Olá {self.nome} aqui está o link: {linesep}{link}') #envia o link para o seguinte chat ID;
                print(self.PegarMensagens) # ecreve no meu terminal /tempo
                print(self.nome) # mostra o nome do infeliz que enviou a mensagem;
                #mensagemEnviada = True  mensagem foi enviada;
                
            elif self.PegarMensagens == "/blumob":
                bot.sendMessage(self.chat_id,f'Olá {self.nome} o horário dos busão tá aqui: {linesep}{link2}')
                print(self.PegarMensagens)
                print(self.nome)

while True: # Loop infinito para bot nunca parar.

    atualizacaoes = bot.getUpdates() #pega todas as informações do bot;
    
                                         #pega o ultimo elemento da variável
    EditAtualizacoes = atualizacaoes[-1] #neste caso serve apenas para simplificar,
                                         #a variável anterior;
    
   

    
    # tratamento de erros que podem acontecer com formatos de arquivos e mensagens diferentes:
    try:
        # para erros de textos editados
        try:
            dadosFormatados = Dados('message', 'text')
        
        except KeyError:
            dadosFormatados = Dados('edited_message', 'text')
    except:
  

        #para erros com sticker 
        try:    
            dadosFormatados = Dados('message', 'sticker')
        except:
            try:    
                try:    
                    dadosFormatados = Dados('message', 'photo')

                except(KeyError):
                    dadosFormatados = Dados('edit_message', 'photo')

            except:
                #para erros de documentos
                try:    
                    dadosFormatados = Dados('message', 'document')
                except: 
                    dadosFormatados = Dados('edited_message', 'document')
    
    if dadosFormatados.data != old_data: # verifica se existe diferença entre as atualizações de msg; 
        mensagemEnviada = False # Mensagem ainda não foi envida;
    else:
        mensagemEnviada = True # mensagem foi enviada
    
    old_data = dadosFormatados.data

    

    if mensagemEnviada == False: #se mensagem não foi enviada; 
        dadosFormatados.enviarMensagens()
            
    sleep(0.000001) #pausa de 1 segundo;
