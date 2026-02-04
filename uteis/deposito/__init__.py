from  uteis import conta
from uteis import acessorios
import datetime
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")


def deposito_dinheiro():
    while True:
        try:
            quantidade_deposito = float(input('Quantidade: $'))


            if quantidade_deposito < 1:
                print('Digite um valor valido\n')

            else:
                extrato_deposito = (
                                    f"{'Sobre Transação':>40}\n\n"
                                    f"Data de transação:    "
                                    f"{datetime.datetime.now().strftime('%a')} - "
                                    f"{datetime.datetime.now().strftime('%d/%m/%Y')}\n"
                                    f"Horário:    "
                                    f"          {datetime.datetime.now().strftime('%H:%M')}\n"
                                    f"Identificador:        s5d5s15d1we15b1s515z77w6d5s4f5f35ee4ww\n"
                                    f"ID transação:         4fs7e8v4d288saf72hth6367sfacv8hls2049vjks\n"
                                    f"Valor transação:      R${quantidade_deposito}\n\n")

                acessorios.armazenar_extrato(deposito=extrato_deposito, saque='')
                conta.saldo_conta += quantidade_deposito
                print('saldo atual: R$',conta.saldo_conta)

                return conta.saldo_conta

        except ValueError:
            print('Este campo é permitido apenas numeros. Digite novamente o valor de deseja depositar\n')

        except KeyboardInterrupt:
            acessorios.saida_programa()

if __name__ == "__main__":
    deposito_dinheiro()


