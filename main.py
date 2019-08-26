import pygame, random

branco = (255,255,255)
preto = (0,0,0)

#Inicialização da fonte
pygame.font.init()
terminou= False
#Dimensões da tela
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

def mostra_titulo():
      font = pygame.font.Font(None, 24)
      text = font.render("S1", 1, preto)
      textpos = text.get_rect(centerx=tela.get_width()/2)
      tela.blit(text, textpos)

while not terminou:
      tela.fill(branco)
      mostra_titulo()
    #Checar os eventos do mouse aqui:
      for event in pygame.event.get(): 
          if event.type == pygame.QUIT:
              terminou = True
         
    #Atualiza o desenho na tela
      pygame.display.update()
#Finaliza a janela do jogo
pygame.display.quit()
