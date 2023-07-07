from copy import deepcopy

class CarroPrototipo:
    def __init__(self):
        self.marca = None
        self.modelo = None

    def clonar(self):
        return deepcopy(self)

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("------------------")


# Criação dos objetos protótipos
carro_prototipo1 = CarroPrototipo()
carro_prototipo1.marca = "Toyota"
carro_prototipo1.modelo = "Corolla"

carro_prototipo2 = CarroPrototipo()
carro_prototipo2.marca = "Honda"
carro_prototipo2.modelo = "Civic"

# Clonagem dos objetos protótipos
carro1 = carro_prototipo1.clonar()
carro2 = carro_prototipo2.clonar()

# Exibição das informações dos carros
carro1.exibir_informacoes()
carro2.exibir_informacoes()