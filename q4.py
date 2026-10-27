num = int(input("Digite um numero inteiro positivo que deseja saber a tabuada: "))
mult = 0
for i in range(1, 11):
    mult = num * i
    print(f"{num} x {i} = {mult}")