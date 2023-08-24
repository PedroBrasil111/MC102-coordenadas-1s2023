###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Picos e Vales I
# Nome:
# RA:
###################################################

# leitura e verificação dos picos e vales
picos = vales = 0 # contadores para núm. de picos e vales
alturas = [] # guarda as alturas lidas
leitura = int(input())
while leitura != 0:
    alturas.append(leitura)
    leitura = int(input())
for i in range(1, len(alturas) - 1): # só pode ser pico/vale da segunda à penúltima altura
    if alturas[i] > alturas[i-1] and alturas[i] > alturas[i+1]:
        picos += 1
    elif alturas[i] < alturas[i-1] and alturas[i] < alturas[i+1]:
        vales += 1

# impressão da saída
print("Quantidade de picos:", picos)
print("Quantidade de vales:", vales)