import sys
import random
import os
from colorama import Fore

def print_field(field, field_len):
    print(end="   ")
    for i in range(65, 65 + field_len):
        print(chr(i), end=" ")
    print()
    j = 1
    for m in field:     #prettier
        print("{:>2}".format(j), end=" ")
        for i in m:
            if i == "#":
                print(Fore.RESET + i, "", end="")
            elif i == "X":
                print(Fore.RED + i, "", end="")
            elif i == "O":
                print(Fore.BLUE + i, "", end="")
        print(Fore.RESET)
        j += 1

def print_winner(symbol):
    if symbol == "X":
        print("Player 1 won")
        return False
    if symbol == "O":
        print("Player 2 won")
        return False

def winner_check(field, field_len, win_condition):
    for x in range(field_len):
        for y in range(field_len): #range len field
            symbol = field[x][y]
            c = 0
            if y < field_len - win_condition:  # len(field)-2  vagy  field_len - (Win condition - 1)
                if not symbol == "#":
                    for i in range(win_condition + 1):  #win_c = 3
                        if field[x][y + i] == symbol:
                            c += 1
                            """ print("Compraing this:", field[x][y + i])
                            print("c:", c)
                            print("x:", x, "y:", y + (i + 1))
                            print("symb:", symbol) """
                if c >= win_condition + 1:
                    return print_winner(symbol)
            c = 0
            if x < field_len - win_condition:
                if not symbol == "#":
                    for i in range(win_condition + 1):  #win_c = 3
                        if field[x + i][y] == symbol:
                            c += 1
                            """ print("Compraing this:", field[x][y + i])
                            print("c:", c)
                            print("x:", x, "y:", y + (i + 1))
                            print("symb:", symbol) """
                if c >= win_condition + 1:
                    return print_winner(symbol)
            c = 0
            if x < field_len - win_condition and y < field_len - win_condition:
                if not symbol == "#":
                    for i in range(win_condition + 1):  #win_c = 3
                        if field[x + i][y + i] == symbol:
                            c += 1
                            """ print("Compraing this:", field[x][y + i])
                            print("c:", c)
                            print("x:", x, "y:", y + (i + 1))
                            print("symb:", symbol) """
                if c >= win_condition + 1:
                    return print_winner(symbol)
            c = 0
            if x > 1 and y < field_len - win_condition:
                if not symbol == "#":
                    for i in range(win_condition + 1):  #win_c = 3
                        if field[x - i][y + i] == symbol:
                            c += 1
                            """ print("Compraing this:", field[x][y + i])
                            print("c:", c)
                            print("x:", x, "y:", y + (i + 1))
                            print("symb:", symbol) """
                if c >= win_condition + 1:
                    return print_winner(symbol)
    #print(c)
    return True

def player_1(field):
    a = input("Which point you wanna choose? (A 2 or 2 A)").split(" ")
    try:
        if a[0].isdigit():
            x = int(a[0]) - 1
            y = ord(a[1].upper()) - 65
            print(x)
        else:
            y = ord(a[0].upper()) - 65
            x = int(a[1]) - 1
        
        if field[x][y] == "#":
            field[x][y] = "X"
        else:
            print("Choose an empty field!")
            player_1(field)      
    except:
        print("Wrong input!")
        player_1(field)   
        
def player_2(field):
    a = input("Which point you wanna choose? (A 2 or 2 A)").split(" ")
    try:
        if a[0].isdigit():
            x = int(a[0]) - 1
            y = ord(a[1].upper()) - 65
            print(x)
        else:
            y = ord(a[0].upper()) - 65
            x = int(a[1]) - 1
        
        if field[x][y] == "#":
            field[x][y] = "O"
        else:
            print("Choose an empty field!")
            player_2(field)
    except:
        print("Wrong input!")
        player_2(field)

def ai_move(field):
    x = random.randrange(0, len(field))
    y = random.randrange(0, len(field))
    if field[x][y] == "#":
        field[x][y] = "O"
    else:
        print("Choose an empty field!")
        ai_move(field)

""" def advanced_ai_move(field):
    x = random.randrange(0, len(field))
    y = random.randrange(0, len(field))
    possible_moves = []
    for m in field:
        tmp = []
        for symbol in m:
            if symbol == "#":
                tmp.append(symbol)
            else:
                tmp.append("")
        possible_moves.append(tmp)
    print("POSSIBLE MOVES:", possible_moves)
    if winner_check(field, 3, 3)
    if field[x][y] == "#":
        field[x][y] = "O"
    else:
        print("Choose an empty field!")
        advanced_ai_move(field)   """  

def init():
    accepted = False
    while not accepted:
        try:
            print("1. Against an opponent\n2. Against AI\n3. Against Advanced AI", "\n" * 3)
            game_type = int(input())
            field_len = input("Enter the size of the field: ")
            field_len = int(field_len)
            win_condition = input("Enter the win condition: ")
            win_condition = int(win_condition) - 1
            if win_condition + 1 > field_len:
                print("Win condition can't be greater than the field!")
                accepted = False
            else:
                return field_len, win_condition, game_type
                accepted = True
        except:
            print("Something went wrong!")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    t = init()
    field_len = t[0]
    win_condition = t[1]
    game_type = t[2]
    field = [["#" for i in range(field_len)] for z in range(field_len)]
    """ field = [['O', 'O', 'X', 'O', '#'],
             ['O', 'X', '#', '#', '#'],
             ['X', '#', 'O', '#', '#'],
             ['#', '#', '#', '#', '#'],
             ['X', 'X', '#', '#', '#']] """
    print_field(field, field_len)
    x = random.randrange(0, 2) 
    while winner_check(field, field_len, win_condition):
        if not any("#" in m for m in field):
            print("It's a tie!")
            break
        if x % 2 == 0:
            print("Player 1 (X) is choosing")
            player_1(field)
            x += 1
        else:
            if game_type == 1:
                print("Player 2 (O) is choosing")
                player_2(field)
                x += 1
            elif game_type == 2:
                print("AI (O) is choosing")
                ai_move(field)
                x += 1
            else:
                print("Advanced AI (O) is choosing")
                advanced_ai_move(field)
                x += 1
        #clear_screen()
        print_field(field, field_len)

if __name__ == "__main__":
    main()