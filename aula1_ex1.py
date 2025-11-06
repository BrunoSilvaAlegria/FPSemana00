#1
hero = ("Bruno", 20, 10, 50)
string = "O herói " + hero[0] + " está no nível " + str(hero[1]) + " com " + str(hero[2]) + " HP e " + str(hero[3]) + " XP."
print(string)

#2
spawm_point = (0,0,0)
x,y,z = spawm_point
print("x: " + str(spawm_point[x]) + " y: " + str(spawm_point[y]) + " z: " + str(spawm_point[z]))

#3
npc = ("Paulinho", 69, ["Bíblia", "Crucifixo", "Pau"])
print(npc[::2])

#4
moedas = (5, 10, 2)
total_moedas = moedas[0] + moedas[1] + moedas[2]
valor_moedas = (5,3,1)
valor_total = 0
for i in range(0, len(moedas)):
    valor_total += moedas[i] * valor_moedas[i]

print('Moedas de cada tipo: ' + 'Ouro: ' + str(moedas[0]) + ' Prata: ' + str(moedas[1])+ ' Bronze: ' + str(moedas[2]))
print("Total de moedas: " , str(total_moedas))
print("Valor por moedas: ", 'Ouro: ' + str(moedas[0] * valor_moedas[0]) + ' Prata: ' + str(moedas[1] * valor_moedas[1])+ ' Bronze: ' + str(moedas[2] * valor_moedas[2]))
print("Valor total: ", valor_total)

#5
scores = ("Ana", "Bruno", "Carla", "David", "Eva")
primeiros = scores[:2]
outros = scores[2:5]
print(primeiros)
print(outros)