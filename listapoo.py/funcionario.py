class Funcionario:
    def __init__(self,nomeFuncionario,cpfFuncionario,valorPorHoraFuncionario):
        
        self.nome=nomeFuncionario
        self.cpf=cpfFuncionario
        self.valorPorHoraFuncionario=valorPorHoraFuncionario
        self.horasTrabalhadas=0
        
    def calcularSalario(self):
        return self.horasTrabalhadas*self.valorPorHoraFuncionario
    
    def incrementarHoras(self,quantidade):
        self.horasTrabalhadas +=quantidade