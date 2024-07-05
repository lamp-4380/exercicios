def dia(d,m,a):
    mes = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",\
           12:"Dezembro"}
    data = input("Escreva uma data(modelo dd/mm/aaaa): ")
    d = data[0:2]
    m = int(data[3:5])
    a = data[6:10]
    return print(d,"de", mes[m], "de", a)
dia(0,0,0)