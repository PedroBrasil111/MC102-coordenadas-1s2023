###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Cupons de Desconto II
# Nome:
# RA:
###################################################

'''
Retorna uma tupla (result, maior), onde result é uma lista em que
cada item é uma tupla com a combinação (compra, cupom) que geram
o desconto máximo e maior é a soma dos descontos de result.
'''
def max_desconto_rec(index, q1, q2, q3, x: list, z: list, compras, desc, result, maior, soma_atual):
    if (index == len(compras) or q1 + q2 + q3 == 0) and soma_atual > maior:
        return desc.copy(), soma_atual
    if index < len(compras):
        if q1 != 0 and compras[index] >= z[0]:
            desc.append((index + 1, 1))
            result, maior = max_desconto_rec(index + 1, q1 - 1, q2, q3, x, z, compras, desc, result,
                                             maior, soma_atual + x[0])
            desc.pop()
        if q2 != 0:
            desc.append((index + 1, 2))
            result, maior = max_desconto_rec(index + 1, q1, q2 - 1, q3, x, z, compras, desc, result,
                                             maior, soma_atual + min((x[1]/100)*compras[index], z[1]))
            desc.pop()
        if q3 != 0 and compras[index] >= z[2]:
            desc.append((index + 1, 3))
            result, maior = max_desconto_rec(index + 1, q1, q2, q3 - 1, x, z, compras, desc, result, 
                                             maior, soma_atual + (x[2]/100)*compras[index])
            desc.pop()
        if q1 + q2 + q3 != 0:
            result, maior = max_desconto_rec(index + 1, q1, q2, q3, x, z, compras, desc, result, 
                                   maior, soma_atual)
    return result, maior

'''
Função para calcular a melhor combinação de cupons para maximizar descontos.
Retorna uma lista onde cada item é uma tupla com a combinação (compra, cupom)
que geram o desconto máximo.
'''
def max_desconto(compras, q1, q2, q3, x1, x2, x3, z1, z2, z3):
    result, _ = max_desconto_rec(0, q1, q2, q3, [x1, x2, x3], [z1, z2, z3], compras, [], [], 0, 0)
    return result

# Leitura de dados
q1, x1, z1, q2, x2, z2, q3, x3, z3, n = [int(input()) for _ in range(10)]
compras = [int(input()) for _ in range(n)]

# Cálculo da melhor atribuição de cupons
result = max_desconto(compras, q1, q2, q3, x1, x2, x3, z1, z2, z3)

# Impressão da resposta
for index, cupom in result:
    print(f"Compra {index}: Cupom {cupom}")
