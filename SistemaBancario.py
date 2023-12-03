'''
        DESAFIO SISTEMA BANCÁRIO COM PYTHON - DIO
        AUTOR: MARIA LIMA

'''
#Tres operações: deposito, saque, extrato

saldo_conta = 0
extrato = ""
numero_saque = 0



while True:


    operacao = input("Selecione umas das opções:\n'S' = Saque\n'D' = Deposito\n'E' = Extrato\nAperte 'Q' para sair\n")

    operacao = operacao.upper()

    if operacao == "S": 
        valor = float(input("Informe o valor do saque: "))

        
        if numero_saque == 3:
            print("Limite de 3 saques por dia atingido")
            
        elif valor > 500:
            print("Limite de R$500 por saque atingido")
            
        elif valor  >  saldo_conta:
           print(f"Valor do saque maior que o saldo em conta. Saldo em conta R${saldo_conta:.2f}\n")
        
        elif valor > 0:
            
            saldo_conta -= valor
            extrato += f"Saque de  R${valor:.2f}\n"
            numero_saque +=1
        
        else:
            print("Informe um valor válido para a operação")

    elif operacao == "D":
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo_conta += valor
            extrato = f"Deposito de: R${valor:.2f}\n"
        else:
            print("Informe um valor maior que 0 (ZERO)")

    elif operacao == "E":
        print("\n===================== EXTRATO =====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo_conta:.2f}")
        print("=====================================================")


    elif operacao == "Q":
        print("Saindo do sistema")
        break

    else:
        print("Operação invalida, por favor, selecione novamente a operação desejada.")
