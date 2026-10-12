#Codigo da classe
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor: #Sem saldo para sacar
            return False
        else:
            self.saldo -= valor #Saque realizado
            return True

    def gerar_extrato(self):
        print(f'Numero: {self.numero}\nCPF: {self.cpf}\nSaldo: R$ {self.saldo}\nNome: {self.nomeTitular}')


    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Tansferencia realizada com sucesso!")



#Codigo do exemplo
conta1 = Conta(123, 12344321, 'Nicolas', 0)
conta2 = Conta(124, 99999999, 'Ana', 500)

print(conta2.transfereValor(conta1, 300))

conta1.gerar_extrato()
print()
conta2.gerar_extrato()







