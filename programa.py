from uteis import deposito, saque, extrato, acessorios, saldo_banco


chance = 3
saldo = saldo_banco.saldo

while True:
    menu = acessorios.menu()

    if menu == 2:
        saldo = saque.saque(saldo)
        chance -= 1

        if chance == 0:
            print('Limite de saque excedido')
            acessorios.sair_programa()

    elif menu == 3:
        saldo = deposito.efetuar_deposito(saldo)

    elif menu == 4:
        extrato.mostrar_extrato()

    elif menu == 5:
        acessorios.sair_programa()



