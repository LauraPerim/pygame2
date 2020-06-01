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


class Player(pygame.sprite.Sprite):
     def __init__ (self):
         pygame.sprite.Sprite.__init__(self)
         img_x = pygame.image.load( "img_x.png")
         self.image=img_x
         self.image = pygame.transform.scale(img_x, (100, 100))
         #self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
         self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
         self.rect.x = 100
        # Sorteia um lugar inicial em y
         self.rect.y =100 
         
class circulo(pygame.sprite.Sprite):
     def __init__ (self):
         pygame.sprite.Sprite.__init__(self)
         img_0 = pygame.image.load( "circulo_0.png")
         self.image=img_0
         self.image = pygame.transform.scale(img_0, (70, 70))
         #self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
         self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
         self.rect.x = 200
        # Sorteia um lugar inicial em y
         self.rect.y =150
'''
x,y=pygame.mouse.get_pos()
x-=mouse_cursor.get_width()/2
y-=mouse_cursor.get_height()/2
screen.blit(mouse_cursor,(x,y))
       
 '''       
         

pygame.init()

WIDTH=500

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True
bg = pygame.image.load("imagem_fundo.png")
bg=pygame.transform.scale(bg,(500,400))



player=Player()
mobs = pygame.sprite.Group()
mobs.add(player)

Circulo=circulo()
cir=pygame.sprite.Group()
cir.add(Circulo)
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(bg, (0, 0))

    mobs.draw(window)
    cir.draw(window)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados




