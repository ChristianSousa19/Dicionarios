n=list()
jogador=dict()
jogador['nome']=str(input("Nome: "))
jogador['partidas']=int(input(f"Quantas partidas {jogador['nome']} jogou?"))

for i in range(0,jogador['partidas']):
    n.append(int(input(f"Quantos gols  {jogador['nome']} fez na {i+1}º partida?")))
jogador['gols']=n[:]
jogador['total']=sum(n)
print(jogador)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*30)
print(f"o{jogador['nome']} jogou {len(jogador['gols'])} partidas")
for l,m in enumerate(jogador['gols']):
    print(f"Na {l+1}ª partida  fez {v} gols ")
    print(f"Foi um total de {jogador['total']} gols")