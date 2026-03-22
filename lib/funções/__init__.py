from classe import ContaBanco

def leiaInt(num):
    while True:
        try:
            entrada = int(input(num))
        except (ValueError, TypeError):
            print('\033[1;91mERRO! Digite um número Inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;91m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return entrada


def salvar_saldo(conta):
    with open('saldo.txt', 'w') as file:
        file.write(f"{conta.id},{conta.titular},{conta.saldo}")

def carregar_conta():
    try:
        with open('saldo.txt', 'r') as file:
            conteudo = file.read().strip()

            if conteudo == '':
                return None

            dados = conteudo.split(',')
            return ContaBanco.ContaBancaria(dados[0], dados[1], float(dados[2]))
    except FileNotFoundError:
        return None
