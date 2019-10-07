import pygame, random
from formatacao import mostra_titulo_aba

titulo = ["ARQUIVOS", "PROCESSOS", "REDE 1", "REDE 2"]


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
      
    @staticmethod  
    def cria_abas(tela, cor):
        lista_de_abas = []
        for i in range(0,4):
            aba_type= i
            aba = Aba(i, cor)
            aba.desenha(tela)
            lista_de_abas.append(aba)
            mostra_titulo_aba(tela, f"{titulo[i]}", (800/4 * aba_type)+100)
        return lista_de_abas
    
    @staticmethod 
    def init_abas(tela, branco, cor):
        tela.fill(branco)
        aba0, aba1, aba2, aba3 = Aba.cria_abas(tela, cor)
