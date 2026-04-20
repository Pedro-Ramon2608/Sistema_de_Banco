from sistemadebanco import models

def leiaInt(num):
    while True:
        try:
            entrada = int(input(num))
        except (ValueError, TypeError):
            print('\nERRO! Digite um número Inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar esse número.')
            return 0
        else:
            return entrada
        
def leiaFloat(num):
    while True:
        try:
            valor = input(num)
            
            valor = valor.replace(".", "").replace(",", ".")
            
            entrada = float(valor)
        except (ValueError, TypeError):
            print("\nERRO! Digite um número Real válido.")
            continue
        except KeyboardInterrupt:
            print("\nUsuário preferiu não digitar um número.")
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
            return models.ContaBancaria(int(dados[0]), dados[1], float(dados[2]))
    except FileNotFoundError:
        return None
