class Agenda:
    def __init__(self,dia,mes,ano,anotacao="Nenhuma tarefa anotada"):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anot = anotacao
    
    def Validar_data(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
    def anotar_tarefa(self,nanot):
        self.anot = nanot
    def Mostrar_anotacao(self):
        print(self.anot)