###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Chuva de Meteoritos
# Nome: 
# RA: 
###################################################

# Leitura de dados
N, M = [int(i) for i in input().split()] # matriz n linhas x m colunas
matriz = [[0] * M for _ in range(N)] # inicialização da matriz com todas as entradas iguais a 0
Q = int(input()) # núm. de entradas

# Processamento
for _ in range(Q):
    x, y, r = [int(i) for i in input().split()] # x,y: coordenadas, r: raio
    # uso de dois for para iterar sobre as entradas da sub-matriz afetada, e
    # uso de max(), min() para não ultrapassar bordas da matriz:
    for i in range(max(0, x - r + 1), min(x + r, len(matriz))):
        for j in range(max(0, y - r + 1), min(y + r, len(matriz[0]))):
            matriz[i][j] += 1

# Impressão da saída
for linha in matriz:
    print(" ".join([str(i) for i in linha]))