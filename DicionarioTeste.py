aluno=dict()
aluno["nome"]=(str(input("nome: ")))
aluno["media"]=(float(input(f"A media de {aluno['nome']}:")))
if aluno['media']>=7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")