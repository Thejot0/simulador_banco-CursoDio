from uteis import extrato, saldo_banco, acessorios
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

def tratar_saque(valor, saldo):

    if valor > saldo:
        print('Saldo insuficiente\n')
        return valor, False

    if valor > 500:
        print('O valor máximo a ser sacado por vez é de R$500\n')
        return saldo, False

    if valor <= 0:
        print('Valor incorreto\n')
        return saldo, False

    return saldo - valor, True


def saque(saldo=0):

    while True:
        try:
            valor = int(input('Digite o valor que deseja sacar: R$'))

            saldo, sucesso = tratar_saque(valor, saldo)


            if sucesso:
                print('Saque efetuado com sucesso!!\n')
                print(saldo)

                lista_saque = [
                    f'Tipo de transação: Saque\n'
                    f'Data: {datetime.now().strftime('%d/%m/%Y')} - {datetime.now().strftime('%A')}\n'
                    f'Valor: R${valor}\n'
                    f'Horario da transação: {datetime.now().time().strftime('%H:%M')}\n'
                ]

                for lista in lista_saque:
                    extrato.extrato_transacao(saque=lista)
                return saldo

        except ValueError:
            print('Digite apenas numeros inteiros\n')

        except KeyboardInterrupt:
            acessorios.sair_programa()


def main():
    saque()

if __name__ == '__main__':
    main()
