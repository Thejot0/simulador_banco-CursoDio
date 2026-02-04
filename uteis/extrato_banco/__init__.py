
def extrato():
    with open(r'C:\Users\the jota\Documents\Cursodio\uteis\deposito\extrato.csv', mode='r', newline='') as extratos:
        for leitura in extratos:
            print(leitura)

    with open(r'C:\Users\the jota\Documents\Cursodio\uteis\saque\extrato.csv', mode='r', newline='') as extratos2:
        for leitura in extratos2:
            print(leitura)


if __name__ == '__main__':
    extrato()
