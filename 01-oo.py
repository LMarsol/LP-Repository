#Exercicio 1 - Orientado a objetos
class Carro:
    def __init__(self, placa, numRodas):
        self.placa = placa
        self.numRodas = numRodas
        
    def setPlaca(self, placa):
        self.placa = placa
    def setNumRodas(self, numRodas):
        self.numRodas = numRodas
    def getPlaca(self):
        return self.placa
    def getNumRodas(self):
        return self.numRodas

carro_1 = Carro("XXXY", 4)

print("O veículo de placa %s possui %d rodas." %(carro_1.getPlaca(), carro_1.getNumRodas()))
