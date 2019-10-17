import psutil

branco = (255,255,255)
preto = (0,0,0)
red = (255,0,0)
darkBlue = (2, 24, 89)

largura_tela, altura_tela = 800, 900
import psutil

infos = []
for p in psutil.process_iter():
    infos.append(
        {"pid" : p.pid,
         "nome": p.name(),
         "rss" : p.memory_info().rss,
         "vms" : p.memory_info().vms})