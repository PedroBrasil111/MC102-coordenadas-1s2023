###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Tradutor de Código Morse
# Nome:
# RA:
###################################################

morse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
}

# Leitura da frase
cripto = input().split(" ")

# Conversão para letras

# Conversão para letras
frase = "" # guarda o resultado
for codigo in cripto:
    if codigo.endswith("*"): # letra corrompida
        letras = []
        for chave in morse.keys(): # busca pelas letras possíveis
            if chave.startswith(codigo.replace("*", "")):
                letras.append(morse[chave])       
        letras.sort()
        # sort desnecessário para versões recentes de Python (iteração sobre dict é feita na ordem)
        frase += "["
        for c in letras:
            frase += c
        frase += "]"
    elif codigo == "": # vem do .split(" ") quando há 2 " " seguidos (espaço entre palavras)
        frase += " "
    else:
        frase += morse[codigo]

# Impressão da frase traduzida
print(frase)
