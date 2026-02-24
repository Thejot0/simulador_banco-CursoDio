from uteis import acessorios, extrato, saldo_banco

from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

def tratar_deposito(valor, saldo=0):

    if valor <= 0:
        return saldo, False, 'Valor invalido. Tente novamente\n'

    return saldo + valor, True, None

def efetuar_deposito(saldo):
    while True:
        try:
            valor = int(input('Digite o valor que deseja depositar: R$'))

            saldo, sucesso, menssagem = tratar_deposito(valor, saldo)

            if sucesso:
                print('Depostio efetuado com sucesso\n')


                lista_deposito = [

                    f'Tipo de transação: Deposito\n'
                    f'Data: {datetime.now().strftime('%d/%m/%Y')} - {datetime.now().strftime('%A')}\n'
                    f'Valor: R${valor}\n'
                    f'Horario da transação: {datetime.now().time().strftime('%H:%M')}\n'
                ]

                for lista in lista_deposito:
                    extrato.extrato_transacao(deposito=lista)
                    return saldo
            else:
                print(menssagem)


        except ValueError:
            print('Digite apenas numeros inteiros')

        except KeyboardInterrupt:
            acessorios.sair_programa()

def main():
    efetuar_deposito(saldo_banco.saldo)

if __name__ == '__main__':
    main()