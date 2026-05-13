# Sistema_de_Banco

🏦 Sistema Bancário Python (CLI)
Um sistema de gerenciamento de conta bancária desenvolvido em Python, utilizando Programação Orientada a Objetos (POO) e persistência de dados em arquivos de texto. O projeto foca na modularização e no tratamento robusto de entradas do usuário.

---
🚀 Funcionalidades

* Persistência de Dados: O saldo e os dados da conta são salvos em um arquivo saldo.txt, permitindo que as informações não sejam perdidas ao fechar o programa.

* Operações Financeiras: Métodos de saque e depósito com validações de segurança (impede saques maiores que o saldo e depósitos negativos).

* Validação de Entradas: Funções customizadas (leiaInt e leiaFloat) que tratam erros de digitação e interrupções do usuário (KeyboardInterrupt).

* Interface Amigável: Menu interativo via terminal com feedback em tempo real das operações.

---
🛠️ Tecnologias e Conceitos

* Python 3.12

* Programação Orientada a Objetos (POO): Uso de métodos especiais como __init__ e __str__ para representação do objeto.

* Modularização: Separação clara de responsabilidades entre main.py, models.py e function.py.

* Manipulação de Arquivos: Uso de with open() para leitura e escrita segura de dados.

* Tratamento de Exceções: Uso extensivo de try/except para garantir a resiliência do sistema.

---
📂 Estrutura do Projeto
```
  ├── main.py              # Ponto de entrada que executa o loop principal

  └── sistemadebanco/      # Pacote contendo a lógica do sistema

    ├── __init__.py      # Inicializador do pacote e lógica de inicialização
    
    ├── models.py        # Definição da classe ContaBancaria
    
    ├── function.py      # Funções utilitárias (Leitura de dados e Persistência)
    
    └── forms.py         # (Reservado para futuras implementações Web/Flask)
    
  ├── saldo.txt            # Arquivo onde os dados da conta são armazenados

  └── README.md            # Documentação do projeto
```

---
🔧 Como executar
1. Clone este repositório:

##### Bash
```
git clone https://github.com/seu-usuario/sistema-bancario.git
```
2. Navegue até a pasta do projeto:

##### Bash
```
cd sistema-bancario
```
3. Execute o arquivo principal:

##### Bash
```
python main.py
```
---
📝 Exemplo de Uso

Ao iniciar, o sistema verifica se existe um arquivo de saldo. Caso não exista, ele cria uma conta padrão para demonstração. O usuário pode então:

Ver Saldo: Exibe os dados formatados do titular e o saldo atual.

Sacar/Depositar: Digitar valores (aceita vírgula ou ponto) que são processados e salvos automaticamente.

---
Objetvos:
- [x] Lógica de Saque e Depósito
- [x] Persistência em .txt
- [ ] Interface com Flask
- [ ] Integração com SQLite
