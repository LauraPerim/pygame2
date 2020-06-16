"""
Insper
Authors: Gianluca Lazzaris Giudici, Laura Batman Perim & Pietro Abe Seixas
Graduating in Computer Engineering
Email: gianlucalg@al.insper.edu.br
Email: laurabp@al.insper.edu.br
Email: pietroas@al.insper.edu.br
"""
#importando as classes necessarias
import pygame 
from os import path
import random
from random import randint
print(randint(0,9))

BLACK = (0, 0, 0)

#criando a classe do x
class Player(pygame.sprite.Sprite): # X
     def __init__ (self,center):
         pygame.sprite.Sprite.__init__(self)
         img_x = pygame.image.load( "img_x.png")
         self.image=img_x
         self.image = pygame.transform.scale(img_x, (140, 140))
       
        
        # Detalhes sobre o posicionamento.
         self.rect = self.image.get_rect()
        
        #  lugar x
         self.rect.center = center

#criando a classe do circulo         
class circulo(pygame.sprite.Sprite): #0
     def __init__ (self,center):
         pygame.sprite.Sprite.__init__(self)
         img_0 = pygame.image.load( "circulo_0.png")
         self.image=img_0
         self.image = pygame.transform.scale(img_0, (120, 90))
     
        
        # Detalhes sobre o posicionamento.
         self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em y
         self.rect.center=center
   
         

         
#iniciando pygame
pygame.init()


# Gera tela principal
window = pygame.display.set_mode((500, 400)) #altura e largura
pygame.display.set_caption('jogo da velha')
tempo=pygame.time.get_ticks()

# ----- Inicia estruturas de dados
game = True #continuar o jogo enquanto o pygame for True
bg = pygame.image.load("imagem_fundo.png") #imagem de fundo
bg=pygame.transform.scale(bg,(500,400)) #posicionamento imagem de fundo


mobs = pygame.sprite.Group() #classe dos X

perguntas=[("Dois pais e dois filhos sentaram-se para comer ovos no café da manhã. Cada um comeu um ovo. Quantos ovos eles comeram no total?"),
           ("Ao nascer e ao morrer sou grande, porém sou pequena no vigor da idade. Quem sou eu? "),
           ("O que todo mundo tem, mas quando precisa vai ao mercado comprar? "),
           ("Qual é a cidade que quando chove molha os bêbados? "),
           ("Qual a cor do cavalo branco de Napoleão? "),
           ("Qual é o tio da cebola? "),
           ("O Sr. Smith tem 4 filhas. Cada uma de suas filhas tem 1 irmão. Quantos filhos Sr. Smith tem ao todo? "),
           ("Uma mulher tem 30 reais pra dividir entre suas duas filhas, que horas são? "),
           ("O que é que tem 3 asas, fica dentro de gaiola, mas não é ave?"),
           ("Qual é o instrumento que não pode ser visto, não pode ser tocado, mas pode ser ouvido? "),
           ("O que vai para cima e para baixo sem sair do lugar? "),
           ("Eu faço a barba várias vezes ao dia, mas continuo barbudo, quem sou eu? R"),
           ("O que tem pescoço, mas não tem cabeça"),("O que a mulher abaixa e a mulher levanta? "),
           ("Como se chama a galinha que pulou de um prédio e ficou louca? ")]

respostas=["3","sombra","canela","bar-sem-lona","preto","tiomate","5","15 pras 2","ventilador","a voz","escada","barbeiro","garrafa", "tampa da privada", "galinha cai-pira"]





#fazendo retangulos para definir o jogo
ret1=pygame.Rect(40,0,180,117)
ret2=pygame.Rect(40,123,150,130)
ret3=pygame.Rect(40,265,180,100)
ret4=pygame.Rect(200,0,130,117)
ret5=pygame.Rect(200,123,112,132)
ret6=pygame.Rect(200,265,130,100)
ret7=pygame.Rect(341,0,120,100)
ret8=pygame.Rect(341,123,140,130)
ret9=pygame.Rect(340,265,130,100)

#Função para sortear posição do CPU:

lista_ret = [ret1, ret2, ret3, ret4, ret5, ret6, ret7, ret8, ret9]

def jogada_cpu(lista_ret):
    
    return random.choice(lista_ret)


                 

cir=pygame.sprite.Group() #definindo grupo circulos




font = pygame.font.SysFont("Consolas", 48) #texto
text = font.render("teste", True, (0, 0, 255))
text2=font.render("0", True, (0, 0, 255))

matriz = [ ["", "", ""], ["", "", ""], ["", "", ""]]

jogX=True  #enquanto o jogador for True
# ===== Loop principal =====
while game:

    a=perguntas[randint(0,14)]
    b=randint(0,14)
    a=perguntas[b]


    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            print(a)

            if True:
                
                if ret1.collidepoint(event.pos):
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[0][0]="X"
                        player=Player(ret1.center)
                        jogX=False
                    else: 
                        matriz[0][0]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
                if ret2.collidepoint(event.pos):
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[1][0]="X"
                        player=Player(ret2.center)
                        jogX=False
                    else: 
                        matriz[1][0]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
                if ret3.collidepoint(event.pos): 
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[2][0]="X"
                        player=Player(ret3.center)
                        jogX=False
                    else: 
                        matriz[2][0]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
                if ret4.collidepoint(event.pos):
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[0][1]="X"
                        player=Player(ret4.center)
                        jogX=False
                    else: 
                        matriz[0][1]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
                
                if ret5.collidepoint(event.pos): 
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[1][1]="X"
                        player=Player(ret5.center)
                        jogX=False
                    else: 
                        matriz[1][1]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
           
                if ret6.collidepoint(event.pos): 
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[2][1]="X"
                        player=Player(ret6.center)
                        jogX=False
                    else: 
                        matriz[2][1]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
                 
                if ret7.collidepoint(event.pos):
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[0][2]="X"
                        player=Player(ret7.center)
                        jogX=False
                    else: 
                        matriz[0][2]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
                 
                if ret8.collidepoint(event.pos):
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")

                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[1][2]="X"
                        player=Player(ret8.center)
                        jogX=False
                    else: 
                        matriz[1][2]="O"
                        player=circulo(jogada_cpu(lista_ret).center)
                        jogX=True
                    mobs.add(player)
                    
                if ret9.collidepoint(event.pos):
                    if jogX:
                        tempo=pygame.time.get_ticks()
                        digite=input("digite a resposta")
                        if digite == respostas[b]:
                            print("acertou")
                            
                        tempo_=pygame.time.get_ticks()
                        tempo_rodada=tempo_-tempo
                        if tempo_rodada>20000:
                            game=False 
                            break
            
                        matriz[2][2]="X"
                        player=Player(ret9.center)
                        jogX=False
                    else: 
                        matriz[2][2]="O"
                        player=circulo((jogada_cpu(lista_ret)).center)
                        jogX=True
                    mobs.add(player)
            else:
                game= False
                break
            
               

         
    
         
    
            
            for i in range(3):
                if(matriz[i][0] == "X" and matriz[i][1] == "X" and matriz[i][2] == "X"):
                    print("GANHOU em linha {}".format(i+1))
                    game= False
                if(matriz[0][1] == "X" and matriz[1][i] == "X" and matriz[2][i] == "X"):
                    print("GANHOU em coluna{}".format(i))
                    game= False
                if(matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X"):
                    print("GANHOU em diag 1")
                    game=False
                if(matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X"):
                    print("GANHOU em diag 2")
                    game=False
            
            for i in range(3):
                if(matriz[i][0] == "O" and matriz[i][1] == "O" and matriz[i][2] == "O"):
                    print("PERDEU em linha {}".format(i))
                    game=False
                if(matriz[0][1] == "O" and matriz[1][i] == "O" and matriz[2][i] == "O"):
                    print("PERDEU em coluna{}".format(i))
                    game=False
                if(matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O"):
                    print("PERDEU em diag 1")
                    game=False
                if(matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O"):
                    print("PERDEU em diag 2")
                    game=False
                        
                            
           
                            
      
                    
                
      
    
        # ----- Gera saídas
    window.fill((255, 255, 255))  
    window.blit(bg, (0, 0))
    if jogX== True:  
        text = font.render("X", True, (0, 0, 255))
    else:
        text = font.render("0", True, (0, 0, 255))
    window.blit(text,(0,0))
        
    now=pygame.time.get_ticks()
    text2=font.render(str((now-tempo)//1000), True, (0, 0, 255))
    window.blit(text2,(50,0))
        #pygame.draw.rect(window,(255,0,0),ret3)  #desenha os retangulos

           
    mobs.draw(window)  #X
    cir.draw(window)  #0
            # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados




