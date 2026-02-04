from uteis import deposito, saque, extrato_banco, acessorios, menu


def projeto():

    while True:
        opcao = menu.opcoes()
        if opcao == 1:
            deposito.deposito_dinheiro()
            continue

        elif opcao == 2:
            saque.saque_saldo()

        elif opcao == 3:
            extrato_banco.extrato()

        elif opcao == 4:
            acessorios.saida_programa()

projeto()