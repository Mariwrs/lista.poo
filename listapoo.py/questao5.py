class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []

    def adicionar_turma(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)
            turma.adicionar_aluno(self)  

    def __repr__(self):
        return f'Aluno({self.nome})'


class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.adicionar_turma(self)  

    def __repr__(self):
        return f'Turma({self.nome})'



a1 = Aluno("João")
a2 = Aluno("Maria")

t1 = Turma("Matemática")
t2 = Turma("História")

t1.adicionar_aluno(a1)
t1.adicionar_aluno(a2)
t2.adicionar_aluno(a1)


print(a1.turmas)  
print(t1.alunos) 