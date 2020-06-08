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

# ----- Inicia estruturas de dados
game = True #continuar o jogo enquanto o pygame for True
bg = pygame.image.load("imagem_fundo.png") #imagem de fundo
bg=pygame.transform.scale(bg,(500,400)) #posicionamento imagem de fundo


mobs = pygame.sprite.Group() #classe dos X



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


                 

cir=pygame.sprite.Group() #definindo grupo circulos




font = pygame.font.SysFont(None, 48) #texto
text = font.render("teste", True, (0, 0, 255))


jogX=True  #enquanto o jogador for True
# ===== Loop principal =====
while game:
    
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if ret1.collidepoint(event.pos):
                if jogX:
                    player=Player(ret1.center)
                    jogX=False
                else: 
                    player=circulo(ret1.center)
                    jogX=True
                mobs.add(player)
            if ret2.collidepoint(event.pos):
                if jogX:
                    player=Player(ret2.center)
                    jogX=False
                else: 
                    player=circulo(ret2.center)
                    jogX=True
                mobs.add(player)
            if ret3.collidepoint(event.pos): 
                if jogX:
                    player=Player(ret3.center)
                    jogX=False
                else: 
                    player=circulo(ret3.center)
                    jogX=True
                mobs.add(player)
            if ret4.collidepoint(event.pos):
                if jogX:
                    player=Player(ret4.center)
                    jogX=False
                else: 
                    player=circulo(ret4.center)
                    jogX=True
                mobs.add(player)#SE COLIDIR COM RET 2
            
            if ret5.collidepoint(event.pos): 
                if jogX:
                    player=Player(ret5.center)
                    jogX=False
                else: 
                    player=circulo(ret5.center)
                    jogX=True
                mobs.add(player)#SE COLIDIR COM RET 2
       
            if ret6.collidepoint(event.pos): 
                if jogX:
                    player=Player(ret6.center)
                    jogX=False
                else: 
                    player=circulo(ret6.center)
                    jogX=True
                mobs.add(player)#SE COLIDIR COM RET 2
             
            if ret7.collidepoint(event.pos):
                if jogX:
                    player=Player(ret7.center)
                    jogX=False
                else: 
                    player=circulo(ret7.center)
                    jogX=True
                mobs.add(player)#SE COLIDIR COM RET 2
             
            if ret8.collidepoint(event.pos):
                if jogX:
                    player=Player(ret8.center)
                    jogX=False
                else: 
                    player=circulo(ret8.center)
                    jogX=True
                mobs.add(player)#SE COLIDIR COM RET 2
                
            if ret9.collidepoint(event.pos):
                if jogX:
                    player=Player(ret9.center)
                    jogX=False
                else: 
                    player=circulo(ret9.center)
                    jogX=True
                mobs.add(player)#SE COLIDIR COM RET 2
           
matriz = [ ["", "", ""], ["", "", ""], ["", "", ""]]
 
matriz[1][1] = "X"
matriz[1][2] = "O"
matriz[0][1] = "X"
matriz[2][1] = "X"
 
#print(matriz)

for i in range(3):
 if(matriz[i][0] == "X" and matriz[i][1] == "X" and matriz[i][2] == "X"):
     print("GANHOU em linha {}".format(i))
for i in range(3):
 if(matriz[0][1] == "X" and matriz[1][i] == "X" and matriz[2][i] == "X"):
     print("GANHOU em coluna{}".format(i))
if(matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X"):
    print("GANHOU em diag 1")
if(matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X"):
    print("GANHOU em diag 2")

             
            
                    
       
                        
  
                
               # print (event.pos)
  

    # ----- Gera saídas
    window.fill((255, 255, 255))  
    window.blit(bg, (0, 0))
    if jogX== True:  
        text = font.render("X", True, (0, 0, 255))
    else:
        text = font.render("0", True, (0, 0, 255))
    window.blit(text,(0,0))
    #pygame.draw.rect(window,(255,0,0),ret3)  #desenha os retangulos

   
    mobs.draw(window)  #X
    cir.draw(window)  #0
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados




