#Se o caminho da esquerda tiver um obstáculo, João vai tentar o caminho da direita.
# Se o caminho da esquerda tiver uma ponte quebrada, João vai procurar outro caminho.
# Se não tiver obstáculo nem ponte quebrada no caminho da esquerda, João seguirá por esse caminho.

caminhoEsquerda = "ponte quebrada"

if (caminhoEsquerda == "obstáculo"):
    print("tentar caminho da direita")
elif (caminhoEsquerda == "ponte quebrada"):
    print("procurar outro caminho")
else:
    print("Seguir por esse caminho")