###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Qual o Melhor Cartão de Crédito?
# Nome:
# RA:
###################################################

# Leitura de dados
x1 = int(input()) # anuidade cashback
x2 = int(input()) # anuidade milhas
z = int(input())  # conversão de 1000 milhas em reais
vp = int(input()) # preço da passagem em reais
m = int(input())  # preço da passagem em milhas
fatura = [int(input()) for _ in range(12)]

# Cálculo das milhas e cashback
# Gratuito
D1 = vp
# Cashback
D2 = vp + x1 - 0.01 * sum(fatura)
# Milhas
milhas = 0 # armazena o total de milhas
for num in fatura: # cálculo das milhas
    milhas += num // 5
D3_r = vp + x2 - (milhas // 1000) * z # D3 usando reais
if m - milhas > 0: # não consegue comprar com milhas
    D3 = D3_r
else:
    D3_m = x2 - (abs(m-milhas) // 1000) * z # D3 usando milhas
    D3 = min(D3_r, D3_m)
# Melhor cartão
if D3 < D2 and D3 < D1:
    MELHOR_CARTAO = 'Cartão Milhas'
elif D2 < D1:
    MELHOR_CARTAO = 'Cartão Cashback'
else:
    MELHOR_CARTAO = 'Cartão Gratuito'

# Impressão da resposta
print("Cartão Gratuito: {:.2f}".format(D1))
print("Cartão Cashback: {:.2f}".format(D2))
print("Cartão Milhas: {:.2f}".format(D3))
print(MELHOR_CARTAO)