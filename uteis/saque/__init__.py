from uteis import conta
from uteis import acessorios
import datetime


def saque_saldo():
    chance_saque = 3
    while True:
        try:
            valor_saque = float(input("Digite o valor que deseja sacar:$"))


            if valor_saque < 1:
                print("O Valor precisa ser maior que zero\n")

            elif valor_saque > 500:
                print('Você so pode sacar R$500 por veze\n')

            elif valor_saque > conta.saldo_conta:
                print('Saldo insuficiente')

            else:
                chance_saque -= 1
                conta.saldo_conta -= valor_saque
                print("Saldo atual: R$", conta.saldo_conta)

                extrato_saque = (
                    f"{'Sobre Transação':>40}\n\n"
                    f"Data de transação:    "
                    f"{datetime.datetime.now().strftime('%a')} - "
                    f"{datetime.datetime.now().strftime('%d/%m/%Y')}\n"
                    f"Horário:    "
                    f"          {datetime.datetime.now().strftime('%H:%M')}\n"
                    f"Identificador:        s5d5s15d1we15b1s515z77w6d5s4f5f35ee4ww\n"
                    f"ID transação:         4fs7e8v4d288saf72hth6367sfacv8hls2049vjks\n"
                    f"Valor transação:      R$ -{valor_saque}\n\n")

                acessorios.armazenar_extrato(saque=extrato_saque, deposito='')

                if chance_saque == 0:
                    print('Quantidade de saque diarias esgotadas')
                    acessorios.saida_programa()
                return conta.saldo_conta


        except ValueError:
            print('Esse campo aceita apenas valores numericos...\n')

        except KeyboardInterrupt:
            acessorios.saida_programa()


if __name__ == "__main__":
    saque_saldo()
