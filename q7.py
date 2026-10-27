positivos = 0
negativos = 0
zeros = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print("Quantidade de positivos:", positivos)
print("Quantidade de negativos:", negativos)
print("Quantidade de zeros:", zeros)