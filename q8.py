aprovados = 0
recuperacao = 0
reprovados = 0
total = 0

nota = float(input("Digite a nota (-1 para encerrar): "))

while nota != -1:

    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        recuperacao += 1
    else:
        reprovados += 1

    total += 1

    nota = float(input("Digite a nota (-1 para encerrar): "))

print("Quantidade de aprovados:", aprovados)
print("Quantidade em recuperação:", recuperacao)
print("Quantidade de reprovados:", reprovados)
print("Total de estudantes cadastrados:", total)