def kml(km,lt):
    lkm = km/lt
    if lkm < 8:
        return print("Gasta muito!")
    elif 8 <= lkm <= 15:
        return print("Econômico!")
    elif lkm > 15:
        return print("Super econômico!")

km = int(input("Digite quantos quilômetros o carro andou: "))
lt = int(input("Digite quantos litros o carro gastou nesses quilômetros: "))
kml(km,lt)