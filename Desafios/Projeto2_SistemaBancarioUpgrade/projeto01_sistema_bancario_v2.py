import os

def menu():
    menu = """
+--------------------+
|        MENU        |
+--------------------+
  [d]  Depositar
  [s]  Sacar
  [e]  Extrato
  [nu] Cria usuario
  [nc] Cria conta
  [lc] Lista contas
  [q] Sair
  >>> """
    return input(menu)

def withdraw (*,balance, withdraw_value, extract, withdrawal_limit_value, number_of_withdrawals, withdrawals_limit):
    exceeded_the_balance = withdraw_value > balance
    exceeded_the_limit = withdraw_value > withdrawal_limit_value
    exceeded_the_withdraw = number_of_withdrawals >= withdrawals_limit

    if exceeded_the_balance:
        print("Você não tem saldo suficiente!")
    elif exceeded_the_limit:
        print("Você tentou sacar mais do que o limite!")
    elif exceeded_the_withdraw:
        print("Número máximo de saques atingido!")
    elif withdraw_value < 0:
        print("Não é possível sacar um valor negativo!")
    elif withdraw_value > 0:
        balance -= withdraw_value
        extract += f"[v SAQUE v]\tR${withdraw_value:.2f}\n"
        print("SAQUE REALIZADO COM SUCESSO!")
        number_of_withdrawals += 1 
           
    return balance, extract

def deposit (balance, deposit_value, extract, /):
    while deposit_value <= 0:
        print("Digite um valor positivo para realizar o depósito!")
        deposit_value = float(input("Digite o valor que deseja depositar: R$"))  

    balance += deposit_value
    extract += f"[^ DEPOSIT ^]\tR${deposit_value:.2f}\n"
    print("DEPÓSITO REALIZADO COM SUCESSO!")
    return balance, extract

def show_extract (balance, /, *, extract):
    print("=" * 10 + "[EXTRATO]" + "=" * 10)
    print("Não foram realizadas movimentações!" if not extract else extract)
    print(f"\nSaldo Total:\tR${balance:.2f}")
    print("=" * 29)

def create_customers(customers):
    cpf = input("Informe o CPF (somente número): ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("CPF já cadastrado!")
        return
    
    name = input("Digite seu nome completo: ")
    birth_date = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    adress = input("Digite seu endereço (logradouro, número - bairro, cidade-sigla estado): ")

    customers.append({"name":name, "birth_date":birth_date, "cpf":cpf, "adress":adress})
    print("CADASTRO REALIZADO COM SUCESSO!")

def filter_customer(cpf, customers):
    filtered_customers = [customers for customers in customers if customers["cpf"] == cpf]
    return filtered_customers[0] if filtered_customers else None

def create_account(agency, account_number, customers):
    cpf = input("Digite o CPF do cliente: ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("CONTA CRIADA COM SUCESSO!")
        return {"agency":agency, "account_number":account_number, "customer":customer}
    
    print("Cliente não encontrado! CPF inválido!")

def list_of_accounts(accounts):
    for account in accounts:
        row = f"""
Agência:\t{account['agency']}
Conta:\t{account['account_number']}
Cliente:\t{account['customer']['name']}
        """
        print("=" * 30)
        print(row)

def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"

    number_of_withdrawals = 0
    balance = 0
    withdrawal_limit_value = 500
    customers = []
    accounts = []
    extract = ""

    while True:
        opcao = menu()

        if opcao == "d":
            deposit_value  = float(input("Digite o valor que deseja depositar: R$"))
            balance, extract = deposit(balance, deposit_value, extract)
        
        elif opcao == "s":
            withdraw_value = float(input("Digite o valor que deseja sacar: R$"))

            balance, extract = withdraw(
                balance=balance,
                withdraw_value=withdraw_value,
                extract=extract,
                withdrawal_limit_value=withdrawal_limit_value,
                number_of_withdrawals=number_of_withdrawals,
                withdrawals_limit=WITHDRAWAL_LIMIT)
        
        elif opcao == "e":
            show_extract(balance, extract=extract)

        elif opcao == "nu":
            create_customers(customers)
        
        elif opcao == "nc":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, customers)

            if account:
                accounts.append(account)

        elif opcao == "lc":
            list_of_accounts(accounts)

        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()