import textwrap


def menu():
    menu = """\n
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tNovo usuário
    [6]\tLista conta
    [7]\tSair
    ==> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito\tR${valor:.2f}\n"
        print("......Depósito realizado!......\n")
    else:
        print("\n---Valor inválido---")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("\nVoce não tem saldo suficiente! ")

    elif excedeu_limite:
        print("\nO valor de saque excede o limite! ")

    elif excedeu_saques:
        print("\nNúmero máximo de saques excedido! ")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saques\tR${valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso! ")
    else:
        print("\O valor informado é inválido")
    return saldo, extrato


def mostra_extrato(saldo, /, *, extrato):
    print("\n=========EXTRATO BANCARIO========")
    print("\nNão foi realizada movimentação. " if not extrato else extrato)
    print(f"\nSaques\t\tR${saldo:.2f}\n")
    print("************************************")


def criar_usuario(usuarios):
    cpf = input("Informe seu CPF(somente números)")
    usuario = verifica_usuario(cpf, usuarios)
    if usuario:
        print("Usuario já existe. ")
        return

    nome = input("Informe seu nome completo! ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe seu endereço (cep, nro, bairro, cidade/sigla estado: ")
    print("Conta criada com sucesso! ")


def verifica_usuario(cpf, usuarios):
    usuarios_verificado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_verificado [0] if usuarios_verificado else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input(" Informe o CPF do usuario ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print("...Conta criada com sucesso!!... ")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("\nUsuario não encontrado operação encerrada.....")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == '1':
            valor = float(input("Informe o valor para depósito. "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == '2':
            valor = float(input("Informe o valor de saque! "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == '3':
            mostra_extrato(saldo, extrato=extrato)
        elif opcao == '4':
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == '5':
            criar_usuario(usuarios)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == '7':
            break
        else:
            print("Opção invalida:..")


main()