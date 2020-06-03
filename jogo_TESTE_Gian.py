import pygame
from sys import exit
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT

#Fazendo todas as def's que serão utilizadas no jogo:

def fazer_xy(posicao):
    global vez
    #coordenadas da posição:
    x, y = posicao

    if vez == "jogador_2":
        pygame.draw.circle(tela, (0, 0, 255), posicao, 50)

    else:
        imagem = pygame.image.load("img_x_2.png").convert_alpha()
        imagem_transformada = pygame.transform.scale(imagem, (100, 100))
        tela.blit(imagem_transformada, (x - 50, y - 50))


def verifica_posicao():

    for posicao in rec:
        if e.type == MOUSEBUTTONDOWN and posicao.collidepoint(posicao_mouse):

            if posicao == rect_1:
                confirmar(0, [100, 100])
            if posicao == rect_2:
                confirmar(1, [300, 100])
            if posicao == rect_3:
                confirmar(2, [500, 100])
            if posicao == rect_4:
                confirmar(3, [100, 300])
            if posicao == rect_5:
                confirmar(4, [300, 300])
            if posicao == rect_6:
                confirmar(5, [500, 300])
            if posicao == rect_7:
                confirmar(6, [100, 500])
            if posicao == rect_8:
                confirmar(7, [300, 500])
            if posicao == rect_9:
                confirmar(8, [500, 500])


def confirmar(lugar, posicao):
    global espaco, vez, escolhe

    if tabuleiro[lugar] == "X":
        print("X")

    elif tabuleiro[lugar] == "O":
        print("O")

    else:
        tabuleiro[lugar] = escolhe
        fazer_xy(posicao)
        print(tabuleiro)

        if vez == "jogador_1":
            vez = "jogador_2" 

        else:
            vez = "jogador_1"

        espaco += 1          
            

def desenha_linhas_fundo():

    pygame.draw.line(tela, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 400), (600, 400), 10)


def verifica_vencedor(coordenadas):

    return((tabuleiro[0] == coordenadas and tabuleiro[1] == coordenadas and tabuleiro[2] == coordenadas) or
        (tabuleiro[3] == coordenadas and tabuleiro[4] == coordenadas and tabuleiro[5] == coordenadas) or
        (tabuleiro[6] == coordenadas and tabuleiro[7] == coordenadas and tabuleiro[8] == coordenadas) or
        (tabuleiro[0] == coordenadas and tabuleiro[3] == coordenadas and tabuleiro[6] == coordenadas) or
        (tabuleiro[1] == coordenadas and tabuleiro[4] == coordenadas and tabuleiro[7] == coordenadas) or
        (tabuleiro[2] == coordenadas and tabuleiro[5] == coordenadas and tabuleiro[8] == coordenadas) or
        (tabuleiro[0] == coordenadas and tabuleiro[4] == coordenadas and tabuleiro[8] == coordenadas) or
        (tabuleiro[2] == coordenadas and tabuleiro[4] == coordenadas and tabuleiro[6] == coordenadas))



def escreve_na_tela(vencedor):

    escrito = "PLAYER {0} WINS".format(vencedor)
    fonte = pygame.font.SysFont("arial", 70)
    
    if vencedor == "TIE":
        tie = fonte.render('DEU VELHA', True, (0, 255, 0), 0)
        tela.blit(tie, (115, 265))
    
    else:
        tie = fonte.render(escrito, True, (0, 255, 0), 0)
        tela.blit(tie, (0, 265))


def recomeca_jogo():
    global espaco, vez, escolhe, estado, tabuleiro

    estado = "jogando"
    vez = "jogador_1"
    escolhe = "X"
    espaco = 0
    tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    tela.fill(0)


def verifica_pontuacao(pontos_1, pontos_2):
    fonte = pygame.font.SysFont('mingliuextbpmingliuextbmingliuhkscsextb', 30)
    jogador_1 = 'jogador_1 = {}'.format(pontos_1)
    jogador_2 = 'jogador_2 = {}'.format(pontos_2)

    escreve_jogador_1 = fonte.render(jogador_1, True, (188, 186, 186))
    escreve_jogador_2 = fonte.render(jogador_2, True, (188, 186, 186))
    tela.blit(escreve_jogador_1, (0, 0))
    tela.blit(escreve_jogador_2, (420, 0))

pygame.init()


#DEFININDO VARIAVÉIS:

tela = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('JOGO DA VELHA')


estado = "jogando"
vez = "jogador_1"
escolhe = "X"
espaco = 0
tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]

rect_1 = Rect((0, 0), (200, 200))
rect_2 = Rect((200, 0), (200, 200))
rect_3 = Rect((400, 0), (200, 200))
rect_4 = Rect((0, 200), (200, 200))
rect_5 = Rect((200, 200), (200, 200))
rect_6 = Rect((400, 200), (200, 200))
rect_7 = Rect((0, 400), (200, 200))
rect_8 = Rect((200, 400), (200, 200))
rect_9 = Rect((400, 400), (200, 200))

rec = [rect_1, rect_2, rect_3, rect_4, rect_5, rect_6, rect_7, rect_8, rect_9]

pontos_1, pontos_2 = 0, 0

print(pygame.font.get_fonts())


#LOOP PRINCIPAL DO JOGO:

while True:
    posicao_mouse = pygame.mouse.get_pos()
    if estado == "jogando":
        desenha_linhas_fundo()
        verifica_pontuacao(pontos_1, pontos_2)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                if vez == "jogador_1":
                    escolhe = "X"
                    verifica_posicao()
                else:
                    escolhe = "O"
                    verifica_posicao()

        if verifica_vencedor("X"):
            print("X WINS")
            escreve_na_tela("X")
            estado = "recomeca_jogot"
            pontos_1 += 1

        elif verifica_vencedor("O"):
            print("O WINS")
            escreve_na_tela("O")
            estado = "recomeca_jogo"
            pontos_2 += 1

        elif espaco >= 9:
            print('EMPATE')
            escreve_na_tela('EMPATE')
            estado = "recomeca_jogo"

    else:
        for x in pygame.event.get():
            if x.type == QUIT:
                pygame.quit()
                exit()
            if x.type == MOUSEBUTTONDOWN:
                recomeca_jogo()
                desenha_linhas_fundo()

    pygame.display.flip()


            
            
            
            

