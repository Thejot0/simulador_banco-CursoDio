from uteis import usuario


def criar_conta(usuarios, contas, numero_conta):
    cpf = input('Digite o CPF do usuário para vincular a conta: ').strip()

    usuarios = usuario.buscar_usuario_por_cpf(cpf, usuarios)

    if not usuario:
        print('Usuário não encontrado.')
        return numero_conta

    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }

    contas.append(conta)

    print('Conta criada com sucesso!')
    return numero_conta + 1


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print("\n==============================")
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
