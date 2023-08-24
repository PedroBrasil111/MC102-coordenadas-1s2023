###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Trem das Onze
# Nome:
# RA: 
###################################################

# Leitura de dados
# primeiro trem
x1 = int(input())
y1 = int(input()) / 60 # conversão de minutos para horas (facilita conta)
w1 = int(input())
z1 = int(input())
# segundo trem
x2 = int(input())
y2 = int(input()) / 60 # conversão de minutos para horas
w2 = int(input())
z2 = int(input())

# Cálculo do tempo gasto para chegar a parada do trem
# hora de saída dos trens
hora1 = x1 + y1
hora2 = x2 + y2
# tempo de cada viagem (em horas)
tempo1 = w1 / z1
tempo2 = w2 / z2
# hora de chegada nas estações
chegada1 = hora1 + tempo1
chegada2 = hora2 + tempo2

# Impressão da resposta
print(chegada1 < hora2 and chegada2 < 11)
