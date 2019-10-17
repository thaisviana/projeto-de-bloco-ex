import pygame
from constants import (branco, preto, red, darkBlue, largura_tela,
altura_tela, infos)

#print(pygame.font.get_fonts())


def mostra_titulo(tela, texto, x, y, tamanho_fonte=16):
      font = pygame.font.SysFont("candara", tamanho_fonte)
      text = font.render(texto, 1, preto)
      textpos = text.get_rect(center=(x, y))
      textpos.left = x
      tela.blit(text, textpos)
      

def mostra_titulo_aba(tela, texto, x):
      font = pygame.font.SysFont("arial", 20)
      text = font.render(texto, 1, branco)
      textpos = text.get_rect(center=(x, 30))
      tela.blit(text, textpos)
      