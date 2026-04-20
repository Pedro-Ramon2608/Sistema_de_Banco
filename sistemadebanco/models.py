# Integrar o banco de dados 


class ContaBancaria:
    """
Cria uma conta bancária
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Acessando a conta {self.id} de {self.titular}...")

    def sacar(self, valor):
        if valor <= 0:
             print(f"Saque inválido.")
        elif valor > self.saldo:
            print(f"Saque RECUSADO! Tentativa de  Saque: R${valor:,.2f}. Saldo: R${self.saldo:,.2f}")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado na conta {self.id}")

    def depositar(self, valor):
            if valor <= 0:
                 print(f"Deposito inválido.")
            else:
                self.saldo += valor
                print(f"Deposito de R${valor:,.2f} realizado na conta {self.id}")


    def __str__(self):
        return f"O número da conta é {self.id}, o nome do titular é {self.titular} e o saldo é de R${self.saldo:,.2f}"
