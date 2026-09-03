#Superclass
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Exibir_Dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

#Classesfilhas
class Professor(Pessoa):
    pass

class Aluno(Pessoa):
    pass

class TAE(Pessoa):
    pass

#Instanciar
aluno1 = Aluno("Alice", 16)
aluno2 = Aluno("Luis", 16)

prof1 = Professor("Sionise", 42)
prof2 = Professor("Josiel", 49)

tae1 = TAE("Rosa", 13)
tae2 = TAE("Teofio", 55)


aluno1.Exibir_Dados()
print()
aluno2.Exibir_Dados()
print()
prof1.Exibir_Dados()
print()
prof2.Exibir_Dados()
print()
tae1.Exibir_Dados()
print()
tae2.Exibir_Dados()


