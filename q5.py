qntd = int(input("Digite a quantidade de numeros que deseja digitar: "))
soma = 0
med = 0

for i in range(qntd):
    num = int(input("Digite um numero inteiro positivo: "))
    soma += num
    if i == 0:
        maior = num
    elif num > maior:
        maior = num

    if i == 0:
        menor = num
    elif num < menor:
        menor = num
med = soma / qntd
print(f"A media dos numeros digitados é: {med:.02f}")
print(f"O maior numero digitado é: {maior}")
print(f"O menor numero digitado é: {menor}")