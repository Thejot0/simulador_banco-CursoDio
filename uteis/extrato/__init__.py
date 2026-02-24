import os
import csv

def extrato_transacao(deposito=None, saque=None):

    arquivo = 'Extrato.csv'
    arquivo_exist = os.path.exists(arquivo)
    fieldname = ['Deposito' 'Saque']

    with open(arquivo, mode='a', encoding='utf-8', newline='') as extratos:
        adicionar = csv.DictWriter(extratos, fieldnames=fieldname)

        if not arquivo_exist:
            adicionar.writeheader()

        adicionar.writerow({'Deposito': deposito, 'Saque': saque})

def mostrar_extrato():
    with open('Extrato.csv', mode='r', encoding='utf-8') as extrato:
        exibir = csv.reader(extrato)

        for linha in exibir:
            for l in linha:
                print(l)
