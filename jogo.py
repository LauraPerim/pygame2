"""
Insper
<<<<<<< HEAD
Authors: Pietro, Gianluca, and Laura Batman Perim
Email: 
Email:
=======
Authors: Gianluca Lazzaris Giudici, Laura Batman Perim & Pietro Abe Seixas
Graduating in Computer Engineering
Email: gianlucalg@al.insper.edu.br
Email: laurabp@al.insper.edu.br
Email: pietroas@al.insper.edu.br
"""

import pygame 
from os import path
import random
from os import path

BLACK = (0, 0, 0)


class Player(pygame.sprite.Sprite): # X
     def __init__ (self,center):
         pygame.sprite.Sprite.__init__(self)
         img_x = pygame.image.load( "img_x.png")
         self.image=img_x
         self.image = pygame.transform.scale(img_x, (100, 100))
         #self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
         self.rect = self.image.get_rect()
        
        #  lugar x
         self.rect.center = center

         
class circulo(pygame.sprite.Sprite): #0
     def __init__ (self,center):
         pygame.sprite.Sprite.__init__(self)
         img_0 = pygame.image.load( "circulo_0.png")
         self.image=img_0
         self.image = pygame.transform.scale(img_0, (100, 70))
         #self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
         self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em y
         self.rect.center=center
         
         
         

         

pygame.init()

WIDTH=500

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True
bg = pygame.image.load("imagem_fundo.png")
bg=pygame.transform.scale(bg,(500,400))


mobs = pygame.sprite.Group()

#dfrnvjnljfnj


ret1=pygame.Rect(0,0,187,117)
ret2=pygame.Rect(0,123,180,130)
ret3=pygame.Rect(0,265,180,100)
ret4=pygame.Rect(200,0,130,100)
ret5=pygame.Rect(200,123,128,132)
ret6=pygame.Rect(200,265,130,100)
ret7=pygame.Rect(341,0,187,117)
ret8=pygame.Rect(341,123,140,130)
ret9=pygame.Rect(340,265,130,100)
                 
Circulo=circulo(ret1.center)
cir=pygame.sprite.Group()
cir.add(Circulo)



font = pygame.font.SysFont(None, 48)
text = font.render("teste", True, (0, 0, 255))


jogX=True
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
            
                
                
                
                
                
            print (event.pos)
       
            

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




