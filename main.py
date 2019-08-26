import pygame, random

branco = (255,255,255)
preto = (0,0,0)

#Inicialização da fonte
pygame.font.init()
terminou= False
#Dimensões da tela
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

dicionario = {'alexandre': 456123789, 'anderson': 1245698456,
              'antonio': 123456456, 'carlos': 91257581,
              'cesar':987458, 'rosemary': 789456125 }

valores_Bytes = dicionario.values()

soma = sum(dicionario.values())
soma = soma/1024/1024
soma_media = soma/len(dicionario)


for i in dicionario.keys():
    valor = dicionario[i]
    converter_mb = valor /1024/1024
    dicionario[i] = round(converter_mb,2)


def mostra_titulo():
      font = pygame.font.Font(None, 24)
      text = font.render("S1", 1, preto)
      textpos = text.get_rect(centerx=tela.get_width()/2)
      tela.blit(text, textpos)
    
def mostra_titulo_h2(texto, y):
      font = pygame.font.Font(None, 20)
      text = font.render(texto, 1, preto)
      textpos = text.get_rect(center=(tela.get_width()/2, y))
      tela.blit(text, textpos)
      
def formata_valores(dicionario, soma):
    soma_indices = 1
    for i in dicionario.keys():
          dicionario[i] = round(dicionario[i],2)
          porcentagem = round((dicionario[i]/soma)*100,2)
          print(f'{soma_indices:^1}     {i:<10}        {dicionario[i]:>9,.2f}      {porcentagem:>11,.2f}')
          mostra_titulo_h2(f'{soma_indices:^1}     {i:<10}        {dicionario[i]:>9,.2f}      {porcentagem:>11,.2f}', 60 + soma_indices*30)
          soma_indices = soma_indices + 1

tela.fill(branco)
mostra_titulo()
mostra_titulo_h2("ACME Inc.           Uso do espaço em disco pelos usuários",30)
mostra_titulo_h2("Nr.    Usuário        Espaço utilizado     % do uso",60)   
formata_valores(dicionario, soma)      
mostra_titulo_h2(f"Total de memoria usada: {round(soma,2)} Mb",300)
mostra_titulo_h2(f"Media de memoria usada: {round(soma_media,2)} Mb",350)

while not terminou:
      
    #Checar os eventos do mouse aqui:
      for event in pygame.event.get(): 
          if event.type == pygame.QUIT:
              terminou = True
         
    #Atualiza o desenho na tela
      pygame.display.update()
#Finaliza a janela do jogo
pygame.display.quit()
