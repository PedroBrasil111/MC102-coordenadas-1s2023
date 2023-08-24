###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Picos e Vales II
# Nome:
# RA:
###################################################

# leitura dos terrenos
terreno_1 = [int(i) for i in input().split()]
terreno_2 = [int(i) for i in input().split()]

# verificação das condições de sequência e quantidade
seq1 = []
seq2 = []
# seq1 e seq2 guardam sequências de vales e picos
for i in range(1, len(terreno_1) - 1): # alturas das "pontas" não podem ser pico/vale
    if terreno_1[i] < terreno_1[i-1] and terreno_1[i] < terreno_1[i+1]:
        seq1.append('v') # vale
    elif terreno_1[i] > terreno_1[i-1] and terreno_1[i] > terreno_1[i+1]:
        seq1.append('p') # pico
for i in range(1, len(terreno_2) - 1):
    if terreno_2[i] < terreno_2[i-1] and terreno_2[i] < terreno_2[i+1]:
        seq2.append('v')
    elif terreno_2[i] > terreno_2[i-1] and terreno_2[i] > terreno_2[i+1]:
        seq2.append('p')

# impressão da saída
if seq1 == seq2:
  print("As sequências e as quantidades de picos e vales são iguais")
elif seq1.count('p') == seq2.count('p') and seq1.count('v') == seq2.count('v'):
  print("As quantidades de picos e vales são iguais")
else:
  print("As sequências e as quantidades de picos e vales são diferentes")