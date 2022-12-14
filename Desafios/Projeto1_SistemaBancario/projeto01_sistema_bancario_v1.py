menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
>>> """

deposito = 0
saque = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar: R$"))

        while deposito <= 0:
            print("Digite um valor positivo para realizar o depósito")
            deposito = float(input("Digite o valor que deseja depositar: R$"))  

        saldo += deposito
        extrato += f"[DEPÓSITO] R${deposito:.2f}\n"
    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Digite o valor que deseja sacar: R$"))
            
            while saque > 500:
                    print("O valor máximo do saque é de R500,00, digite um valor válido")
                    saque = float(input("Digite o valor que deseja sacar: R$"))
            
            if saque > saldo:
                print("Saque inválido! Dinheiro insuficiente na conta.")
            else:
                saldo -= saque
                extrato += f"[SAQUE] R${saque:.2f}\n" 
                numero_saques += 1        
        else:
            print("Limite de saque atingido! Volte amanhã.")
    
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print("==== EXTRATO ====")
            print(extrato)
            print(f">> Saldo total: R${saldo:.2f}")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")