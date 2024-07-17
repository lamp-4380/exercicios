class Nota_Fiscal:
    def __init__(self,num,tipo,serie,cnpj,rs,data,vp,icms,frete,ipi,vt="Desconhecido"):
        self.numero = num
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razsoc = rs
        self.data = data
        self.valprod = vp
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valt = vt
    def obterNumero(self):
        print(self.numero)
    
    def obterDataEmissao(self):
        print(self.data)
    
    def alterarRazaoSocial(self,nrs):
        self.razsoc = nrs
        print(f"Nova Razão Social: {self.razsoc}")
    
    def calcularValorTotal(self):
        self.valt = self.vp + self.frete + self.ipi + self.icms
        print(f"Valor total: {self.valt}")