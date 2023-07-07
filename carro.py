class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar_carro(self):
        print(f"O {self.marca} {self.modelo} está ligado")


carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

carro1.ligar_carro()
carro2.ligar_carro()