import regex as re


def nome_usuario():
    while True:
        nome = input('Digite seu nome: ').strip()

        if len(nome) < 3:
            print('Digite um nome válido.')
        elif re.fullmatch(r"^[\p{L}]+(?: [\p{L}]+)*$", nome):
            return nome
        else:
            print('Esse campo só permite letras.')


def data_nascimento():
    while True:
        data = input('Digite sua data de nascimento (DDMMAAAA): ').strip()

        if len(data) != 8 or not data.isnumeric():
            print('Digite uma data válida com 8 números.')
        else:
            return f'{data[:2]}/{data[2:4]}/{data[4:]}'


def cpf_usuario():
    while True:
        cpf = input('Digite o CPF (somente números): ').strip()

        if not cpf.isnumeric() or len(cpf) != 11:
            print('CPF inválido.')
        else:
            return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def validar_endereco(dados):
    if not all(dados.values()):
        return False, 'Nenhum campo pode ficar vazio.'

    if not dados['cidade'].isalpha() or not dados['estado'].isalpha():
        return False, 'Cidade e estado devem conter apenas letras.'

    return True, None


def endereco_usuario():
    while True:
        try:
            estado = input('Estado: ').strip()
            cidade = input('Cidade: ').strip()
            bairro = input('Bairro: ').strip()
            rua = input('Rua: ').strip()
            numero = int(input('Número da casa: '))

            dados = {
                'estado': estado,
                'cidade': cidade,
                'bairro': bairro,
                'rua': rua,
                'numero': numero
            }

            valido, erro = validar_endereco(dados)

            if not valido:
                print(erro)
                continue

            return dados

        except ValueError:
            print('Número da casa deve ser inteiro.')


def buscar_usuario_por_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    nome = nome_usuario()
    endereco = endereco_usuario()
    data = data_nascimento()
    cpf = cpf_usuario()

    if buscar_usuario_por_cpf(cpf, usuarios):
        print('Já existe um usuário com esse CPF.')
        return

    usuarios.append({
        'nome': nome,
        'endereco': endereco,
        'data': data,
        'cpf': cpf
    })

    print('Usuário cadastrado com sucesso!')
