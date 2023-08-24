###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - A Caçada I
# Nome:
# RA:
###################################################

# Leitura da matriz de plataformas
plataformas = []
n = int(input())
for _ in range(n):
    plataformas.append(list(input()))

# Simulação do caminho
vel = 1 # andando p/ direita: vel = 1, esquerda: vel = -1
petiscos = x = y = 0 # inicialização dos petiscos e coordenadas
passos = [] # guarda os índices da linha atual que já foram visitados
while len(passos) != len(plataformas[0]) and x != len(plataformas):
    # while acaba se visitou todos os índices ou caiu em um buraco na última linha
    if y not in passos:
        passos.append(y) # posição visitada pela primeira vez
    if plataformas[x][y] == ".": # buraco
        x += 1
        passos.clear() # nova linha
    else:
        if plataformas[x][y] == "*": # petisco
            petiscos += 1
            plataformas[x][y] = "_" # remove petisco da matriz
        y += vel # movimenta p/ esquerda ou direita
        if y == len(plataformas[0]) - 1 or y == 0: # atingiu uma das bordas laterais
            vel = -vel # sentido do movimento inverte

# Impressão da saída
print(petiscos)