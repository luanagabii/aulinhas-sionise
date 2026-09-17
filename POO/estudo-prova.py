class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

aluno1 = Aluno("luana", 17)
aluno1.Exibir_dados()
