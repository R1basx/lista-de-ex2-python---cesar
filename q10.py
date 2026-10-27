saldo = 1000

opcao = 0

while opcao != 4:

    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        valor = float(input("Digite o valor do depósito: R$ "))

        saldo += valor

        print("Depósito realizado com sucesso!")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 3:
        valor = float(input("Digite o valor do saque: R$ "))

        if valor <= saldo:
            saldo -= valor

            print("Saque realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Saldo insuficiente!")

    elif opcao == 4:
        print("Caixa eletrônico encerrado. Obrigado!")

    else:
        print("Opção inválida!")