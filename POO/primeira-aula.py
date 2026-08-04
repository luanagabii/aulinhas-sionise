class Aluno:
    def __init__(self, nome, matricula, idade, sexo, cpf, rg, turma, email, tel, endereço, ):
        #atributo (caracteristicas de classe/objeto)
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.turma = turma
        self.email = email
        self.telefone = tel
        self.endereço = endereço

class Professor:
    def __init__(self, nome, idade, sexo, cod_contrato, lattes, siep, email, tel, disciplina, formação,):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cod_contrato = cod_contrato
        self.lattes = lattes
        self.siep = siep
        self.email = email
        self.tel = tel
        self.disciplina = disciplina
        self.formação = formação
        

