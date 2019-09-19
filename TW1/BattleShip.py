import os
import time
import math

BOARD_SIZE = 11
NUMS = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
LETTERS = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
shipTypes = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
shipLengths = [5, 4, 3, 3, 2]

class Ship:
    def __init__(self, shipType, shipLength, coords, tiles):   #coords = [x1, y1, x2, y2] 1 = start, 2 = end
        self.shipType = shipType
        self.shipLength = shipLength
        self.coords = coords
        self.tiles = tiles

class Board:
    board = []
    ships = []
    forbiddenTiles = []

    def __init__(self, dimension):
        self.dimension = dimension
        self.createBoard(dimension)

    def createBoard(self, N):
        tmpB = []
        for i in range(N):
            tmp = []
            for j in range(N):
                tmp.append("~")
            tmpB.append(tmp)
        self.board = tmpB

    def refreshBoard(self):
        j = 0
        while j < len(self.board):
            self.board[0][0] = "  "
            self.board[0][j] = LETTERS[j]
            if j > 9:
                self.board[j][0] = NUMS[j]
            else:
                self.board[j][0] = " " + NUMS[j]
            j += 1
        for i in self.board:
            print(" ".join(i))

    def canBeLaid(self, ship):      #collision check
        canbelaid = True
        print(self.forbiddenTiles)
        for i in range(ship.shipLength):
            for j in range(len(self.forbiddenTiles)):
                if ship.tiles[i] == self.forbiddenTiles[j]:
                    print("Collided!")
                    canbelaid = False
                            #print(ship.tiles[i])
            print("The Ship: {}".format(ship.tiles))
        #TODO
    
    def placeShip(self, shipType, shipLength, coords, tiles):
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        #print(coords)
        if y1 > y2:
            (y1, y2) = (y2, y1)
        if x1 > x2:
            (x1, x2) = (x2, x1)
        
        if x1 == x2:
            for i in range(shipLength):
                self.board[x1][y1 + i] = "O"
                tmp = []
                tmp.append(x1)
                tmp.append(y1 + i)
                tiles.append(tmp)
        else:
            for i in range(shipLength):
                self.board[x1 + i][y1] = "O"
                tmp = []
                tmp.append(x1 + i)
                tmp.append(y1)
                tiles.append(tmp)
        coords = [x1, y1, x2, y2]
        self.ships.append(Ship(shipType, shipLength, coords, tiles))
        self.forbiddenTiles += tiles

class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

def initialize():
    p = []
    i = 0
    while i < 2:
        name = input("Player {} name: ".format(i + 1))
        p.append(Player(name, Board(BOARD_SIZE)))
        i += 1
    return p

def buildPhase(playerID):
    print("Build Phase")
    print(playerID.name + "'s Board: ")
    playerID.board.refreshBoard()
    accepted = 0
    placed = 0
    while placed < 5:
        tiles = []
        while accepted < 4:
            print("Place the {} (length: {}) (Usage: B 2 B 6)".format(shipTypes[placed], shipLengths[placed]))
            Points = input().split(" ")
            Coords = ["x1", "y1", "x2", "y2"]
            if len(Points) == 4:
                for i in range(1, len(LETTERS)):
                    if Points[0] == LETTERS[i]:
                        Coords[1] = int(NUMS[i])
                        accepted += 1
                        break
                for i in range(1, len(NUMS)):
                    if Points[1] == NUMS[i]:
                        Coords[0] = int(NUMS[i])
                        accepted += 1
                        break
                for i in range(1, len(LETTERS)):
                    if Points[2] == LETTERS[i]:
                        Coords[3] = int(NUMS[i])
                        accepted += 1
                        break
                for i in range(1, len(NUMS)):
                    if Points[3] == NUMS[i]:
                        Coords[2] = int(NUMS[i])
                        accepted += 1
                        break
            if (Coords[0] == Coords[2]) or (Coords[1] == Coords[3]):     #check if its a line
                d = math.sqrt((pow((Coords[0] - Coords[2]), 2)) + (pow((Coords[1] - Coords[3]), 2)))
                if d == shipLengths[placed] - 1:
                    #print(playerID.board.canBeLaid(Coords, Ship.shipLengths[placed]))
                    if placed == 0:
                        playerID.board.placeShip(shipTypes[placed], shipLengths[placed], Coords, tiles)
                        playerID.board.refreshBoard()
                    else:
                        if playerID.board.canBeLaid(playerID.board.ships[placed - 1]):
                            #print(d)
                            playerID.board.placeShip(shipTypes[placed], shipLengths[placed], Coords, tiles)
                            playerID.board.refreshBoard()
                            print("Successfully placed the ship!")
                            print("Ship type: {} and it's coords: {}".format(playerID.board.ships[placed].shipType, playerID.board.ships[placed].coords))
                            print("Tiles: {}".format(playerID.board.ships[placed].tiles))
                            print("TILE 1: {}".format(tiles[0]))
                            #time.sleep(2.5)
                            #os.system("cls")
                            #print(Points)
                        else:
                            accepted = 0
                else:
                    accepted = 0
            else:
                accepted = 0
            #print("Coords: {}".format(Coords))
        placed += 1
        accepted = 0
    #NUMS[a]
    for ship in playerID.board.ships:
        print(ship.tiles)

print("** BattleShip 2019 edition **")
players = initialize()
buildPhase(players[0])
#buildPhase(players[1])

time.sleep(1)