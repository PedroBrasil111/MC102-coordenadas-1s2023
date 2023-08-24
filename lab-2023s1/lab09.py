###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Classificação de Imagens
# Nome:
# RA:
###################################################

# Leitura de dados e processamento
n = int(input())
aparicoes = {} # dict onde chave: nome do animal, valor: núm. de aparições
for _ in range(n):
    animais = input().split()
    for animal in animais:
        if animal not in aparicoes:
            aparicoes[animal] = 1 # inicialização da chave
        else:
            aparicoes[animal] += 1
preditos = [] # guarda os animais preditos (50%+ de predição)
for animal in sorted(aparicoes.keys()): # animais em ordem alfabética
    if aparicoes[animal] >= 0.5 * n:
        preditos.append(animal)

# Impressão da saída
if not preditos:
    print("Nenhum animal foi predito")
else:
    print("Animais preditos: ", end="")
    for i in range(len(preditos) - 1): # imprime todos menos último (facilita formatação)
        print(f"{preditos[i]}, ", end="")
    print(preditos[len(preditos) - 1]) # imprime último
