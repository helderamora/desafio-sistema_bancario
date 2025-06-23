menu = """
------ Sistem Bancário ------ 

        [d] Deposito
        [s] Saque
        [e] Extrato
        [q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
saque = 0
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito! "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"


        else:    
            print("Operação falhou! Você precisa digitar algum valor! ")


    elif opcao == "s":
        valor = float(input("Informe o valor do sacar: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação invalida! Saldo insuficiente. ")

        elif excedeu_limite:
            print("Operação invalida! Você do saque excedeu o limite. ")

        elif excedeu_saldo:
            print("Operação invalida! Número de saques diario excedido. ")        

        elif excedeu_saques:
            print("Operação invalida! Você excedeu o limite diádrio para saque. ")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
        
    elif opcao == "q":
        break   
    
    else: 
        print("Operação invalida! Selecione a opção desejada. \n") 
