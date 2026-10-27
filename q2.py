num = int(input("Digite um numero inteiro positivo: "))
contador = 1
npar = 0

for i in range(1, num + 1):
    if contador % 2 == 0:
        print(contador)
        npar += 1
    contador += 1

print("Quantidade de numeros pares: ", npar)