from sistemadebanco.function import carregar_conta, salvar_saldo, leiaInt, leiaFloat
from sistemadebanco.models import ContaBancaria
import os

def iniciar_sistema():
    if not os.path.exists("saldo.txt"):
        c1 = ContaBancaria(112, "Pedro Ramon", 2500)
        salvar_saldo(c1)

    c1 = carregar_conta()

    while True:
        if c1 is None:
            print("Nenhuma conta encontrada.")
        opcao = leiaInt('''
    Selecione a opção desejada:
    [ 1 ] Ver saldo
    [ 2 ] Sacar 
    [ 3 ] Depositar
    [ 4 ] Encerrar
    Sua opção: ''')
        if opcao == 1:
            print(c1)
        elif opcao == 2:
            saque = leiaFloat("Digite o valor que deseja sacar: R$")
            c1.sacar(saque)
            salvar_saldo(c1)
        elif opcao == 3:
            deposito = leiaFloat("Digite o valor que deseja depositar: R$")
            c1.depositar(deposito)
            salvar_saldo(c1)
        elif opcao == 4:
            break
        else:
            print("Erro! O número digitado está inválido.")
