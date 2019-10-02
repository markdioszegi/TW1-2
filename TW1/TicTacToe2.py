import sys

def print_field(field):
    for i in field:
        print(i)

def winner_check(field, field_len, win_condition):
    c = 0
    for x in range(field_len):
        for y in range(field_len): #range len field
            if y < field_len - win_condition:  # len(field)-2  vagy  field_len - (Win condition - 1)
                if field[x][y] == field[x][y + (i + 1)] == "O":
                    if field[x][y] == "X":
                        print("Player 1 won")
                        return False
                    if field[x][y] == "O":
                        print("Player 2 won")
                        return False
                c += 1
            """ if x < field_len - win_condition:
                for i in range(win_condition + 1):
                    if field[x][y] == field[x + (i + 1)][y]:
                        if field [x][y] == "X":
                            print("Player 1 won")
                            return False
                        if field[x][y] == "O":
                            print("Player 2 won")
                            return False
            if x < field_len - win_condition and y < field_len - win_condition:
                for i in range(win_condition + 1):
                    if field[x][y] == field[x + (i + 1)][y + (i + 1)]:
                        if field [x][y] == "X":
                            print("Player 1 won")
                            return False
                        if field[x][y] == "O":
                            print("Player 2 won")
                            return False
            if x > 1 and y < field_len - win_condition:
                if field[x][y] == field[x-1][y+1] == field[x-2][y+2]:
                    if field [x][y] == "X":
                        print("Player 1 won")
                        return False
                    if field[x][y] == "O":
                        print("Player 2 won")
                        return False """
    print(c)
    return True

""" def winner_check(field, field_len, win_condition):
    for x in range(field_len):
        for y in range(field_len): #range len field
            if y < field_len - 2:  # len(field)-2  vagy  field_len - (Win condition - 1)
                if field[x][y] == field[x][y+1] == field[x][y+2]:
                    if field [x][y] == "X":
                        print("Player 1 won")
                        return False
                    if field[x][y] == "O":
                        print("Player 2 won")
                        return False
            if x < field_len - 2:
                if field[x][y] == field[x+1][y] == field[x+2][y]:
                    if field [x][y] == "X":
                        print("Player 1 won")
                        return False
                    if field[x][y] == "O":
                        print("Player 2 won")
                        return False
            if x < field_len - 2 and y < field_len - 2:
                if field[x][y] == field[x+1][y+1] == field[x+2][y+2]:
                    if field [x][y] == "X":
                        print("Player 1 won")
                        return False
                    if field[x][y] == "O":
                        print("Player 2 won")
                        return False
            if x > 1 and y < field_len - 2:
                if field[x][y] == field[x-1][y+1] == field[x-2][y+2]:
                    if field [x][y] == "X":
                        print("Player 1 won")
                        return False
                    if field[x][y] == "O":
                        print("Player 2 won")
                        return False
    return True """

def player_1(field):
    a = input("Which field you wanna choose?").split(" ")
    try:
        x = int(a[0])
        y = int(a[1])
        if field[x][y] == "#":
            field[x][y] = "X"
        else:
            print("Chose an empty field!")
            player_1(field)      
    except:
        print("Use this format pls: 2 2")
        player_1(field)   
        
def player_2(field):
    a = input("Which field you wanna choose?").split(" ")
    try:
        x = int(a[0])
        y = int(a[1])
        if field[x][y] == "#":
            field[x][y] = "O"
        else:
            print("Chose an empty field!")
            player_2(field)      
    except:
        print("Use this format pls: 2 2")
        player_2(field)   

def main():
    field_len = input("Enter the size of the field: ")
    field_len = int(field_len)
    win_condition = input("Enter the win condition: ")
    win_condition = int(win_condition) - 1
    print(win_condition)
    #field = [["#" for i in range(field_len)] for z in range(field_len)]
    field = [['#', '#', 'O', '#', '#'],
             ['#', '#', '#', '#', '#'],
             ['#', 'O', 'X', 'O', 'O'],
             ['#', '#', '#', '#', '#'],
             ['#', '#', '#', '#', '#']]
    print_field(field)
    x = 0 
    while winner_check(field, field_len, win_condition) == True:
        if x % 2 == 0:
            print("player1")
            player_1(field)
            print_field(field)
            x += 1
        else:
            print("player2")
            player_2(field)
            print_field(field)
            x +=1

main()