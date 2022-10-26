import datetime
trabalhador=dict()
idade=0

trabalhador["nome"]=(str(input("nome: ")))
trabalhador["Idade"]=int(input("Ano de nascimento"))
idade=datetime.datetime.now().year-trabalhador['Idade']
trabalhador["ctps"]=int(input("Carteira de trabalho[DIGITE 0 SE NÃO HOUVER]"))
if trabalhador['ctps']!=0:
  trabalhador["contrato"]=int(input("Ano de contratação: "))
  trabalhador["Salario"]=float(input("Salario R$:"))
  trabalhador["cnh"]=trabalhador['contrato']+35-datetime.datetime.now().year



print(f"Nome do individuo e {trabalhador['nome']}")
print(f"{trabalhador['nome']} tem {idade} Anos de idade")
print(f"ctps tem o valor {trabalhador['ctps']} ")
print(f"{trabalhador['nome']} foi contratado no ano de {trabalhador['contrato']}")
print(f"{trabalhador['nome']} possui o salario de {trabalhador['Salario']}")
print(f"{trabalhador['nome']} irá se aposentar com {trabalhador['cnh']} anos")


