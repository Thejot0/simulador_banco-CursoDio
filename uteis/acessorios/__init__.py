import sys
from time import sleep

def sair_programa():

    print('Saindo do programa', end='')
    for ponto in range(3):
        print('.', end='')
        sleep(0.7)
    sys.exit()

def linha(tamanho= 55):
    print( '_' * tamanho)


def menu():

    while True:
        try:

            linha()
            print(

                # '[1] Criar usuario\n'
                '[2] Sacar\n'
                '[3] Depositar\n'
                '[4] Extrato\n'
                '[5] Sair'

            )
            linha()

            escolha = int(input('Escolha uma opção: '))

            if escolha > 5 or escolha < 1:
                print('Escolha uma opção valida')

            else:
                return escolha

        except ValueError:
            print('Digite apenas numeros inteiros')

        except KeyboardInterrupt:
            sair_programa()



def main():
    linha()
    sair_programa()
    menu()


if __name__ == '__main__':
    main()
