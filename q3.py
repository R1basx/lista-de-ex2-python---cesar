num = int(input("Digite um numero inteiro positivo: "))
contador = 1
soma = 0

for i in range(1, num + 1):
    soma += contador
    contador += 1

print("A soma dos numeros de 1 a ", num, " é: ", soma)