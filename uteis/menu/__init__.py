from uteis import acessorios


def opcoes():
    menu =('--------------------------\n'
           '[1] Depositar\n'
           '[2] Sacar\n'
           '[3] Extrato\n'
           '[4] Sair\n'
           '--------------------------')
    print(menu)

    while True:
        try:
            escolher_servico = int(input('Escolha uma opção valida: '))

            if escolher_servico > 5 or escolher_servico < 1:
                print('Digite apenas opções validas...\n')

            else:
                return escolher_servico

        except KeyboardInterrupt:
            acessorios.saida_programa()

        except ValueError:
            print('Este campo permite apenas numeros inteiros...\n')

if __name__ == '__main__':
    opcoes()