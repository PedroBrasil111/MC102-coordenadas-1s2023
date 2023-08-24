###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - A Caçada II
# Nome:
# RA:
###################################################

'''
Função para simular o caminho do gato, essa função deve
ser implementado de forma recursiva. A função Recebe uma
matriz representando as plataformas e a posição (linha,coluna)
do gato. A função deve retornar o numero de petiscos recolhidos.
'''
def simula_caminho(mat, lin, col):
    petiscos_linha = 0 # guarda quantos petiscos há na linha atual
    petiscos_baixo = [0] # guarda quantos petiscos podem ser obtidos abaixo da linha atual
    if lin == len(mat):
        return 0
    if mat[lin][col] == ".":
        return simula_caminho(mat, lin + 1, col)
    for j in range(col, -1, -1): # caminho à esquerda de (lin, col)
        if mat[lin][j] == "|": # se atingir uma parede, encerra a iteracão
            break
        if mat[lin][j] == "*":
            petiscos_linha += 1
        elif mat[lin][j] == ".":
            petiscos_baixo.append(simula_caminho(mat, lin + 1, j))
    for j in range(col + 1, len(mat[0])): # caminho à direita de (lin, col)
        if mat[lin][j] == "|":
            break
        if mat[lin][j] == "*":
            petiscos_linha += 1
        elif mat[lin][j] == ".":
            petiscos_baixo.append(simula_caminho(mat, lin + 1, j))
    return petiscos_linha + max(petiscos_baixo)

# Leitura da matriz de plataformas
plataformas = []
n = int(input())
for _ in range(n):
    plataformas.append(list(input()))

# Simulação do caminho
frutas = simula_caminho(plataformas, 0, 0)

# Impressão da saída
print(frutas)

