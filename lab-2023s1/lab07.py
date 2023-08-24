###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Cupons de Desconto I
# Nome:
# RA:
###################################################

# Leitura de dados
x1, z1, x2, z2, x3, z3, n = [int(input()) for _ in range(7)]
compras = [int(input()) for _ in range(n)]

# Cálculo da melhor atribuição de cupons
maior = 0 # maior desconto
# iterando sobre as contas para cada cupom
for i in range(n):
    for j in range(n):
        if i != j: # compras diferentes
            for k in range(n):
                if k not in [i, j]: # compras diferentes
                    desconto_1 = x1 if compras[i] > z1 else 0
                    desconto_2 = min((x2/100) * compras[j], z2)
                    desconto_3 = (x3/100) * compras[k] if compras[k] > z3 else 0
                    desconto_total = desconto_1 + desconto_2 + desconto_3
                    if desconto_total > maior:
                        maior = desconto_total
                        index = (i + 1, j + 1, k + 1) # núm. das compras

# Impressão da resposta
print(f"Cupom 1: {index[0]}\nCupom 2: {index[1]}\nCupom 3: {index[2]}")