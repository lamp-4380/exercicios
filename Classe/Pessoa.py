class Pessoa:
    def __init__(self,mat,nom,i):
        self.matricula = mat
        self.nome = nom
        self.idade = i
    
class Aluno(Pessoa):
    def __init__(self,mat,nom,i,notas,media):
        super().__init__(mat,nom,i,notas,media)
        self.notas = notas
        self.media = media
    
    def FaltarAula(self):
        print("Fugindo da sala...")
    
    def FazerProvas(self):
        print("Porque a questão 11 é sempre a mais difícil...")

class Professor(Pessoa):
    def __init__(self,mat,nom,i,formacao,disciplina,carga_horaria,salario):
        super().__init__(mat,nom,i,formacao,disciplina,carga_horaria,salario)
        self.form = formacao
        self.dis = disciplina
        self.ch = carga_horaria
        self.sal = salario
    
    def ensinar(self):
        print("então, a Geometria Angular...")
    
    def expulsar_Aluno(self):
        print("Pra Companhia, agora!")
    
    def seAposentar(self):
        print("Não aguento mais esses alunos...")