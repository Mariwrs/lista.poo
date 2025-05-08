from funcionario import Funcionario

Funcionario1 = Funcionario("lucas","11134578900",25.50)

print("nome:",Funcionario1.nome)
print("cpf:",Funcionario1.cpf)
print("valor por hora",Funcionario1.valorPorHoraFuncionario)

Funcionario1.incrementarHoras(8)
print("horas trabalhadas depois do 1 incremento:",Funcionario1.horasTrabalhadas)

Funcionario1.incrementarHoras(4)
print("horas trabalhadas depois 2 incremento:",Funcionario1.horasTrabalhadas)

salario = Funcionario1.calcularSalario()
print("Salário calculado:",salario)