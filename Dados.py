import random
import operator
import time
jogador={"jogador1":random.randint(1,6),
         "jogador2":random.randint(1,6),
         "jogador3":random.randint(1,6),
         "jogador4":random.randint(1,6)}

ranking=list()
for c,h in jogador.items():
    print(f"{c} Tirou {h} no dado")
    time.sleep(1)
ranking=sorted(jogador.items(),key=operator.itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
 print('-='*30)
 print("RANKIG")
 print(f"{i+1}ºLugar: {v[0]} com {v[1]}")
 time.sleep(1)
