import pygame, random

class Aba():
    def __init__(self, aba_type, cor):
      self.largura = 200
      self.altura = 60
      self.x = 200 * aba_type
      self.y = 0
      self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
      self.cor = cor
    def desenha(self, tela):
      pygame.draw.rect(tela, self.cor, self.area)
