"""
SISTEMA BANCARIO    : Dio.me
PROGRAMADOR         : Anthony Samuel Sobral de Freitas
"""
menu = """
\t\t   =================================================
\t\t    [d] Depositar  [s] Sacar  [e] Extrato  [q] Sair
\t\t   =================================================
=> """
saldo = 0
limite = 500
extrato = ""
numero_saque = 0 
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES
        if  excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido ")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é invalido")
    elif opcao == "e":
        print("\n===========Extrato===============")
        print("Não foi realizada movimentação." if not extrato else extrato)
        print(f"\nSaldo em conta R$ {saldo:.2f}")
        print("=================================")
    elif opcao == "q":
        break
    else:
        print("Selecione uma opção válida ")