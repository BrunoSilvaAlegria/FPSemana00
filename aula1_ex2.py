#1
mapa = [
    ["Sala 0,0", "Sala 0,1", "Sala 0,2"],
    ["Sala 1,0", "Sala 1,1", "Sala 1,2"],
    ["Sala 2,0", "Sala 2,1", "Sala 2,2"]
    ]

posicao = (1,2) #linha 2(1) e coluna 3(2)

print(mapa[posicao[0]][posicao[1]]) #Sala 1,2

#2
"""
CIMA = 0
ESQUERDA = 1
BAIXO = 2
DIREITA = 3

bordas_mapa = [
    [(False,False,True,True), (False,True,True,True), (False,True,True,False),
    (True,False,True,True), (True,True,True,True), (True,True,True,False),
    (True,False,False,True), (True,True,False,True), (True,True,False,False)
    ]
]
"""

pos = (1,1)
x,y = pos
salas_visitadas = []
salas_visitadas.append(pos)

print("Começo!")
print("Posição inicial -", mapa[pos[x]][pos[y]])

while True:

    print("W - Cima | S - Baixo | A - Esquerda | D - Direita")
    command = input("Para onde quer ir?\n").strip().lower()

    if command == "w":
        #if bordas_mapa[y][x][CIMA]:
            y -= 1
            pos = (x,y)
            salas_visitadas.append(pos)
            print("Posição atual -", mapa[pos[x]][pos[y]])
        #else: print("Não podes sair do mapa!")
    elif command == "s":
        #if bordas_mapa[y][x][BAIXO]:
            y += 1
            pos = (x,y)
            salas_visitadas.append(pos)
            print("Posição atual -", mapa[pos[x]][pos[y]])
        #else: print("Não podes sair do mapa!")
        
    elif command == "a":
        #if bordas_mapa[y][x][ESQUERDA]:
            x -= 1
            pos = (x,y)
            salas_visitadas.append(pos)
            print("Posição atual -", mapa[pos[x]][pos[y]])
        #else: print("Não podes sair do mapa!")
    elif command == "d":
        #if bordas_mapa[y][x][DIREITA]:
            x += 1
            pos = (x,y)
            salas_visitadas.append(pos)
            print("Posição atual -", mapa[pos[x]][pos[y]])
        #else: print("Não podes sair do mapa!")
    elif command == "sair":
        for i in range(0, len(salas_visitadas)):
            print("Salas visitadas:", salas_visitadas[i])
        break
    else:
        print("Não entendi, repita!!!")