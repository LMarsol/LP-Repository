#Exercicio 1 - Estruturado

veiculos = {
    "Carro Y": {"Placa": "XXXY", "NumRodas": 4},
    "Moto X": {"Placa": "XXYX", "NumRodas": 2},
    "Carro Z": {"Placa": "XYXX", "NumRodas": 3}
    }

for veiculo in veiculos:
    placa = veiculos[veiculo]["Placa"]
    numRodas = veiculos[veiculo]["NumRodas"]
    print("O veículo de placa %s possui %d rodas." %(placa, numRodas))
