###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Escolha da Missão
# Nome: 
# RA: 
###################################################

# leitura de dados
nvl = int(input())  # nível
atq = int(input())  # ataque
dfs = int(input())  # defesa
ouro = int(input()) # ouro inicial

# Escolha da missão
# Ordenar as missões em ordem decrescente de ganho absoluto de ouro permite o uso de elif's
if nvl >= 5 and atq >= 40 and dfs >= 50 and ouro >= 50: # missão 5
    ouro += 80 # 130 - 50
    missao = 5
elif nvl >= 5 and atq >= 50 and dfs >= 50: # missão 6 com ataque suficiente
    ouro += 60
    missao = 6
elif nvl >= 3 and ouro >= 50: # missão 3
    ouro += 50 # 100 - 50
    missao = 3
elif nvl >= 3 and atq >= 20 and dfs >= 30: # missão 4 sem comprar bota
    ouro += 40
    missao = 4
elif nvl >= 5 and dfs >= 50: # missão 6 sem ataque suficiente
    ouro += 30
    missao = 6
elif atq >= 30 and dfs >= 10: # missão 1
    ouro += 25
    missao = 1
elif nvl >= 3 and ouro >= 20: # missão 4 comprando bota
    ouro += 20 # 40 - 20
    missao = 4
elif dfs >= 30 and ouro >= 30: # missão 2
    ouro += 10 # 40 - 30
    missao = 2
else: # não é capaz de fazer nenhuma das missões
    missao = 0

# Impressão da missão escolhida
print('missão escolhida:', missao)
print('moedas de ouro:', ouro)