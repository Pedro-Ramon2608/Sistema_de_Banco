from time import sleep

class ContaBancaria:
    """
Cria uma conta bancária
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Acessando a conta {self.id} de {self.titular}...")
        sleep(1)

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque RECUSADO! Tentativa de  Saque: R${valor:,.2f}. Saldo: R${self.saldo:,.2f}")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado na conta {self.id}")

    def depositar(self, valor):
            self.saldo += valor
            print(f"Deposito de R${valor:,.2f} realizado na conta {self.id}")


    def __str__(self):
        return f"O número da conta é {self.id}, o nome do titular é {self.titular} e o saldo é de R${self.saldo:,.2f}"
