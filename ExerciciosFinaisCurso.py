##calcular e exibir a quantidade de XP ganhos com base no nível do monstro e na dificuldade da batalha.
nivel = 45
dificudade = 40
multiplicador = 100

xpGanhos = nivel * dificudade * multiplicador

print(f"Voce ganhou {xpGanhos} XP")

##Calculadora de salario
salarioBruto = 2000
beneficios = 250
imposto = ""

if ( 0<salarioBruto<1100):
    imposto = salarioBruto * 0.05
elif (1100.01<salarioBruto<2500):
    imposto = salarioBruto * 0.10
else: imposto = salarioBruto * 0.15

resultado = (salarioBruto-imposto) + beneficios

print(f"O salario a receber e de {resultado}")

salarioBruto2 = 5500
beneficios2 = 250

def calcularimposto(salario):
    if 0< salario <1100:
        taxa = 0.05
    elif 1100.01< salario <2500:
        taxa = 0.10
    else: taxa = 0.15
    return taxa*salario

imposto2 = calcularimposto(salarioBruto2)
resultado2 = (salarioBruto2-imposto2) + beneficios2

print(f"O salario a receber e de {resultado2}")

##Mensagem de Boas Vindas para escolha de Pokemon
pokemon = 3
pokemonchose = ""

if (pokemon == 1):
    pokemonchose = "Bulbasaur"
elif (pokemon == 2):
    pokemonchose = "Charmander"
elif (pokemon == 3):
    pokemonchose = "Pikachu"
elif (pokemon == 4):
    pokemonchose = "Mewtwo"
else: pokemonchose = ""

print(f"You chose {pokemonchose} as your starting Pokemon.")

##Collecting Treasures in the Dungeon
totalRooms = 7
roomsTreasure = [2,4,7]
roomsMonsters = [3,6,8]

for sala in range (1,totalRooms+1):
    withTreasure = sala in roomsTreasure
    withMonsters = sala in roomsMonsters
    if (withTreasure):
        print(f"Treasure in room {sala}")
    elif (withMonsters):
        print(f"Monsters in room {sala}")

##Geração de Biomas em um Mundo de Blocos
scams = 4
minerals = ["Carvao", "Ferro", "Diamante", "Pedra"]

for i in range (0, scams +1):
    mineralIndex = i %len(minerals)
    print(f"{i} : {minerals[mineralIndex]}")

##Combinando Nomes de Pokémons
def combinateNames(name):
    proName = name + "saur"
    return proName

initialName = "Ivy"
finishName = combinateNames(initialName)

print(finishName)

