import pygame, random
from aba import Aba
from constants import (branco, preto, red, darkBlue, largura_tela,
altura_tela, dicionario)

#Inicialização da fonte
pygame.font.init()
terminou= False
#Dimensões da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))

valores_Bytes = dicionario.values()
soma = sum(dicionario.values())
soma = soma/1024/1024
soma_media = soma/len(dicionario)

for i in dicionario.keys():
    valor = dicionario[i]
    converter_mb = valor /1024/1024
    dicionario[i] = round(converter_mb,2)
    
def mostra_titulo(texto, y, fonte=20):
      font = pygame.font.Font(None, fonte)
      text = font.render(texto, 1, preto)
      textpos = text.get_rect(center=(tela.get_width()/2, y))
      #textpos.left = 100
      tela.blit(text, textpos)

def mostra_titulo_aba(texto, x):
      font = pygame.font.Font(None, 24)
      text = font.render(texto, 1, branco)
      textpos = text.get_rect(center=(x, 30))
      tela.blit(text, textpos)
      
def formata_valores(dicionario, soma):
    soma_indices = 1
    for i in dicionario.keys():
          dicionario[i] = round(dicionario[i],2)
          porcentagem = round((dicionario[i]/soma)*100,2)
          #print(f'{soma_indices:^1}     {i:<10}        {dicionario[i]:>15,.2f}      {porcentagem:>11,.2f}')
          mostra_titulo(f'{soma_indices:^1}     {i:<10}        {dicionario[i]:>9,.2f}      {porcentagem:>11,.2f}', 160 + soma_indices*30)
          soma_indices = soma_indices + 1

def cria_abas():
    lista_de_abas = []
    for i in range(0,4):
        aba_type= i
        aba = Aba(i, darkBlue)
        aba.desenha(tela)
        lista_de_abas.append(aba)
        mostra_titulo_aba(f"ABA {i}", (largura_tela/4 * aba_type)+100)
    return lista_de_abas

def mostra_conteudo_aba_0():
    mostra_titulo("ABA 0", 100, 24)
    mostra_titulo("ACME Inc.           Uso do espaço em disco pelos usuários",130)
    mostra_titulo("Nr.    Usuário        Espaço utilizado     % do uso",160)   
    formata_valores(dicionario, soma)      
    mostra_titulo(f"Total de memoria usada: {round(soma,2)} Mb",400)
    mostra_titulo(f"Media de memoria usada: {round(soma_media,2)} Mb",450)


tela.fill(branco)
aba0, aba1, aba2, aba3 = cria_abas()
mostra_conteudo_aba_0()


while not terminou:
      
    #Checar os eventos do mouse aqui:
      for event in pygame.event.get(): 
          if event.type == pygame.QUIT:
             terminou = True
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
             pos = pygame.mouse.get_pos()
             if aba1.area.collidepoint(pos):
                 tela.fill(branco)
                 aba0, aba1, aba2, aba3 = cria_abas()
                 mostra_titulo("ABA 1", 300, 24)
             if aba2.area.collidepoint(pos):
                 tela.fill(branco)
                 aba0, aba1, aba2, aba3 = cria_abas()
                 mostra_titulo("ABA 2", 300, 24)
             if aba3.area.collidepoint(pos):
                 tela.fill(branco)
                 aba0, aba1, aba2, aba3 = cria_abas()
                 mostra_titulo("ABA 3", 300, 24)
             if aba0.area.collidepoint(pos):
                 tela.fill(branco)
                 aba0, aba1, aba2, aba3 = cria_abas()
                 mostra_conteudo_aba_0()
         
    #Atualiza o desenho na tela
      pygame.display.update()
#Finaliza a janela do jogo
pygame.display.quit()
