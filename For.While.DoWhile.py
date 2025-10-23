#Exercício 1: Contar de 1 a 5
#for i in range (1,6):
#    print(i)

#Exercício 2: Números Pares
#for i in range (0,21, 2):
#    print(i)

#Exercício 5: Numero ao contrario
#n = 5
#for i in range (n,0,-1):
#    print(i)

#Exercício 3: Soma de Números
n1 = 5
soma = 0
#for i in range (1,n1 + 1):
#    soma += i
#print("A soma de 1+2+3+4+5 e : ", soma)

#Exercício 4: Tabuada
n2 = 7
#for i in range (1,11,1):
#    print(n2,"x",i,"=",(n2*i))

#Exercício 5: Fatorial
n3 = 5
fatorial = 1
#for i in range (1,n3 + 1):
#    fatorial *= i
#   print(fatorial)

#Exercício 6: Desenhar um Triângulo
n4 = 4
n5 = ""
#for i in range (1,n4 + 1):
#    n5 += "*"
#    print(n5)

#Exercício : Contar Vogais
palavra = "programaçao"
vogais = "aeiou"
contador = 0
for i in range (1,len(palavra),1):
    if palavra[i] in vogais:
        contador += 1
#print(contador)

#Exercício 11: Calcular Potências
base = 2
expoente = 3
resultado = 1
for i in range (1, expoente + 1):
    resultado *= base
#print(resultado)

#Exercício 11: Números Múltiplos
n6 = 20
m = 5
for i in range(m,n6 + 1,m):
    print(i)