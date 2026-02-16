import sys
from time import sleep
import csv
import os


def linha(tamanho = 40):
    quantidade = '_' * tamanho

    print(quantidade, '\n')

def saida_programa():

    print('Saindo do programa', end='')
    for p in range(3):
        print('.', end='')
        sleep(0.4)
    sys.exit()

def armazenar_extrato(deposito = None, saque = None):

    arquivo = 'extrato.csv'
    arquivo_exist = os.path.exists(arquivo)

    with open(arquivo, 'a', encoding='utf-8', newline='') as extrato:
        titulo = {'Deposito':deposito, 'Saque':saque}
        adicionar = csv.DictWriter(extrato, fieldnames=titulo)

        if not arquivo_exist:
            adicionar.writeheader()

        adicionar.writerow(titulo)

if __name__ == '__main__':
    linha()
    saida_programa()