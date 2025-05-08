class ContaCorrete:
    def __init__(self,cliente,saldo):
        
        self.cliente =cliente
        self.saldo =saldo
        
    def depositar(self,valor):
        self.saldo += valor 
        
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
        