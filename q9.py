quantidade = int(input("Quantidade de números: "))

for i in range(quantidade):

    num = int(input("Digite um número: "))

    if i == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

diferenca = maior - menor

print("Maior número:", maior)
print("Menor número:", menor)
print("Diferença:", diferenca)