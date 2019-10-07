import pygame, random
from aba import Aba
import os
import time
from constants import (branco, preto, red, darkBlue, largura_tela,
altura_tela, infos)
from formatacao import mostra_titulo, mostra_titulo_aba

#Inicialização da fonte
pygame.font.init()
terminou= False
#Dimensões da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
soma_rss = sum([i["rss"] for i in infos])/1024/1024/1024
soma_vms = sum([i["vms"] for i in infos])/1024/1024/1024
soma = 0
soma_media = 0
titulo = ["ARQUIVOS", "PROCESSOS", "REDE 1", "REDE 2"]

def formata_valores(soma):
    soma_indices = 1
    for item in infos:
          vms = item["vms"]/1024/1024
          rss = item["vms"]/1024/1024
          mostra_titulo(tela, f'{item["pid"]}',100, 160 + soma_indices*22)
          mostra_titulo(tela, f'{item["nome"]}', 160, 160 + soma_indices*22)
          mostra_titulo(tela, f'{round(vms,2)} MB',400, 160 + soma_indices*22)
          mostra_titulo(tela, f'{round(rss,2)} MB',500, 160 + soma_indices*22)
          mostra_titulo(tela, f'{round((vms/(soma_vms*1024))*100,2)} %',620, 160 + soma_indices*22)
          mostra_titulo(tela, f'{round((rss/(soma_rss*1024))*100,2)} %',700, 160 + soma_indices*22)
          soma_indices = soma_indices + 1

def cria_abas():
    lista_de_abas = []
    for i in range(0,4):
        aba_type= i
        aba = Aba(i, darkBlue)
        aba.desenha(tela)
        lista_de_abas.append(aba)
        mostra_titulo_aba(tela, f"{titulo[i]}", (largura_tela/4 * aba_type)+100)
    return lista_de_abas

def mostra_conteudo_aba_0(conta_segundos):
    mostra_titulo(tela, f'ARQUIVOS - {conta_segundos}s',100, 100, 24)
    mostra_titulo(tela, f'index',40,160)
    mostra_titulo(tela, f'Nome Arquivo',100,160)
    mostra_titulo(tela, f'Tamanho',240,160)
    mostra_titulo(tela, f'Data Modificação',340,160)
    mostra_titulo(tela, f'Data Criação',590,160)
    lista = os.listdir()
    soma_indices = 1
    for i in lista: 
        if os.path.isfile(i):
            mostra_titulo(tela, f'{soma_indices}',40, 160 + soma_indices*22)
            mostra_titulo(tela, f'{i}', 100, 160 + soma_indices*22)
            mostra_titulo(tela, f'{round(os.stat(i).st_size/1024,2) }KB',240, 160 + soma_indices*22)
            mostra_titulo(tela, f'{time.ctime(os.stat(i).st_mtime)}',340, 160 + soma_indices*22)
            mostra_titulo(tela, f'{time.ctime(os.stat(i).st_atime)}',590, 160 + soma_indices*22)
            soma_indices += 1

def mostra_conteudo_aba_1(conta_segundos):
    mostra_titulo(tela, f'PROCESSOS - {conta_segundos}s',100, 100, 24)
    mostra_titulo(tela, f'PID',100,160)
    mostra_titulo(tela, f'NOME',160,160)
    mostra_titulo(tela, f'VMS',400,160)
    mostra_titulo(tela, f'RSS',500,160) 
    mostra_titulo(tela, f'% VMS',620,160)
    mostra_titulo(tela, f'% RSS',700,160) 
    formata_valores(soma)
    mostra_titulo(tela, f"Total de memoria RSS usada: {round(soma_rss,2)} Gb",100,870)
    mostra_titulo(tela, f"Total de memoria VMS usada: {round(soma_vms,2)} Gb",100,850)
    
def init_abas():
    tela.fill(branco)
    aba0, aba1, aba2, aba3 = cria_abas()

conta_clocks = 0
conta_segundos = 0

tela.fill(branco)
aba0, aba1, aba2, aba3 = cria_abas()
mostra_conteudo_aba_0(conta_segundos)
aba_selecionada = 0

#Indica o relogio de aparecimento de quadros do jogo
clock = pygame.time.Clock()
#Variavel para contar quantas esperas de 50Hz ou 0,02s

while not terminou:
      
    #Checar os eventos do mouse aqui:
      for event in pygame.event.get(): 
          if event.type == pygame.QUIT:
             terminou = True
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
             pos = pygame.mouse.get_pos()
             if aba1.area.collidepoint(pos):
                 init_abas()
                 aba_selecionada = 1
                 mostra_conteudo_aba_1(conta_segundos)
             if aba2.area.collidepoint(pos):
                 aba_selecionada = 2
                 init_abas()
                 mostra_titulo(tela, f'ABA 2 | {conta_segundos}s',100, 300, 24)
             if aba3.area.collidepoint(pos):
                 aba_selecionada = 3
                 init_abas()
                 mostra_titulo(tela, f'ABA 3 | {conta_segundos}s',100, 300, 24)
             if aba0.area.collidepoint(pos):
                 aba_selecionada = 0
                 init_abas()
                 mostra_conteudo_aba_0(conta_segundos)
      conta_clocks += 1
      #A cada 50 cont_clocks, temos 1s (0,02s x 50 = 1s)
      if conta_clocks == 50:
          if conta_segundos >= 0:
              conta_segundos += 1
          conta_clocks = 0   
          init_abas()
          if aba_selecionada == 0:
              mostra_conteudo_aba_0(conta_segundos)
          elif aba_selecionada == 1:
              mostra_conteudo_aba_1(conta_segundos)
          elif aba_selecionada == 2:
              mostra_titulo(tela, f'ABA 2| {conta_segundos}s',100, 300, 24)
          elif aba_selecionada == 3:
              mostra_titulo(tela, f'ABA 3| {conta_segundos}s',100, 300, 24)
      
      #Atualiza o desenho na tela
      pygame.display.update()
      #Configura 50 atualizações de tela por segundo
      clock.tick(50)
#Finaliza a janela do jogo
pygame.display.quit()
