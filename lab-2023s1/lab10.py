#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Carrinho Elétrico
# Nome:
# RA:
#####################################################

# Leitura do circuito
n, m = [int(i) for i in input().split()]
pista = []
for i in range(n):
    linha = input().split()
    pista.append(linha)
    if "-" in linha:
        # x, y são as coordenadas do carro,
        # inicializadas com as coordenadas da chegada:
        x, y = i, linha.index("-")

# Leitura e processamento das instruções
voltas = 0 # núm. de voltas
comando = input()
while comando != "0":
    comando = comando.split()
    vezes, direcao = int(comando[0]), comando[1]
    if direcao == "O": # oeste (move uma coluna p/ esquerda: y -= 1)
        for _ in range(vezes):
            if y-1 >= 0 and pista[x][y-1] != "#": # não sai da matriz e não atinge barreira
                y -= 1
                if pista[x][y] == "-": # linha de chegada
                    voltas += 1
    elif direcao == "L": # leste (move uma coluna p/ direita: y += 1)
        for _ in range(vezes):
            if y+1 < m and pista[x][y+1] != "#": # não sai da matriz e não atinge barreira
                y += 1
                if pista[x][y] == "-":
                    voltas += 1
    elif direcao == "N": # norte (move uma linha p/ cima: x -= 1)
        for _ in range(vezes):
            if x-1 >= 0 and pista[x-1][y] != "#": # não sai da matriz e não atinge barreira
                x -= 1
                if pista[x][y] == "-":
                    voltas += 1
    elif direcao == "S":
        for _ in range(vezes): # sul (move uma linha p/ baixo: x += 1)
            if x+1 < n and pista[x+1][y] != "#": # não sai da matriz e não atinge barreira
                x += 1
                if pista[x][y] == "-":
                    voltas += 1
    comando = input()

# Impressão da saída
print('Voltas completadas:', voltas)