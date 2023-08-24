###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Novos Algoritmos de Ordenação
# Nome:
# RA:
###################################################

'''
Recebe uma lista de elementos e retorna o número de trocas realizadas pelo algoritmo Seleção e Inserção.
Essa função deve imprimir a lista de elementos após cada inserção.
'''
def selecao_e_insercao(lista):
    trocas = 0 # guarda núm. total de trocas
    for i in range(len(lista)): # posição que deve ser colocado o próximo menor número
        menor, index = lista[i], i # guardam menor número e seu índice
        for j in range(i + 1, len(lista)): # buscando menor número na porção não ordenada
            if lista[j] < menor:
                menor, index = lista[j], j
        if index != i: # só troca se o menor não estiver na posição correta
            for j in range(index, i, -1): # passa números entre i e index uma posição p/ direita
                trocas += 1
                lista[j] = lista[j-1]
            lista[i] = menor # lista agora está ordenada até a posição i
            print(lista)
    return trocas


'''
Recebe uma lista de elementos e retorna o número de trocas realizadas pelo algoritmo Bubble Up and Down.
Essa função deve imprimir a lista de elementos sempre que o algoritmo fizer a verificação da completa lista.
'''
def bubble_up_and_down(lista):
    trocas = 0 # guarda núm. total de trocas
    trocou = True # ao fim de cada iteração: True se elementos trocaram de lugar, False caso contrário
    reverso = 1 # reverso == 1 se ordenação ocorre da esq. p/ dir., == 0 no sentido contrário
    while trocou:
        trocou = False
        if reverso: # equivale a reverso != 0
            for j in range(len(lista) - 1): # esquerda para direita
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocas += 1
                    trocou = True
        else:
            for j in range(len(lista) - 1, 0, -1): # direita para esquerda
                if lista[j-1] > lista[j]:
                    lista[j], lista[j-1] = lista[j-1], lista[j]
                    trocas += 1
                    trocou = True
        if trocou:
            print(lista)
        reverso = (reverso + 1) % 2 # alterna reverso entre 0 e 1
    return trocas

# Leitura da sequência
lista = [int(a) for a in input().split()]

# Execução dos algoritmos de ordenação e impressão dos resultados
print("Algoritmo Seleção e Inserção:")
X = selecao_e_insercao(lista.copy())
print("Trocas realizadas:", X)
print()
print("Algoritmo Bubble Up and Down:")
Y = bubble_up_and_down(lista.copy())
print("Trocas realizadas:", Y)