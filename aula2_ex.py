"""#exemplo
def squares(value):
    ret = []
    for i in range(0, value):
        ret.append(i * i)
    return value * value, ret #sq, array_of_values
sq, array_of_values = squares(5)
print(sq)
print(array_of_values)"""

#1
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


while True:
    n1 = int(input("What's the first number? -> "))
    n2 = int(input("What's the second number? -> "))
    operation = input("What's the operation(add, sub, mult, div)? -> ")
    
    if operation == "out": break
    elif operation == "add":
            print(add(n1,n2))
            pass
    elif operation == "sub":
            print(sub(n1,n2))
            pass
    elif operation == "mult":
            print(mult(n1,n2))
            pass
    elif operation == "div":
            print(div(n1,n2))
            pass
    else: print("Not a valid operation! Try again.")

#2

rooms = [
        ["A", "B", "C"], 
        ["D", "E", "F"], 
        ["G", "H", "I"]
        ] 

#[(False, True, False, False)] -> [(NORTH, WEST, SOUTH, EAST)] -> [(0, 1, 2, 3)]
room_exits = [
    [(False, False, False, True), (False, True, True, True), (False, True, True, False)],
    [(False, False, True, True), (True, True, True, True), (True, False, False, False)],
    [(True, False, False, False), (True, False,False, True), (False, True, False, False)]
]

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

position = (1, 1) # E

def move(dir_text, dir_index, y_inc, x_inc):
    global position #necessary to change current position

    x,y = position
    if command == dir_text:
        if room_exits[y][x][dir_index]:
            x += x_inc
            y += y_inc
            position = (x,y)
            print("Moved ", dir_text, " to room ", rooms[y][x])
        else:
             print("You can't move ", dir_text)
        return True
    return False 


print("Start!")
print("Initial room:", rooms[position[0]][position[1]])

while True:
    x, y = position
    
    command = input("Which direction would you like to go?\n(north, south, east or west)\n-> ")

    if command == "exit":
        print("Goodbye...")
        break
    elif move("north", NORTH, -1, 0):
        pass
    elif move("west", WEST, 0, -1):
        pass
    elif move("south", SOUTH, 1, 0):
        pass
    elif move("east", EAST, 0, 1):
        pass
    else: print("Not sure about that one, chief...")        