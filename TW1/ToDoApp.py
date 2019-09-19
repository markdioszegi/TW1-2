import sys
import io

def loadFile():
    lines = []
    with open("TW1\\todolist.txt", "r") as file:
        lines = file.readlines()
        file.close()
    return lines

def saveFile(lines):
    with open("TW1\\todolist.txt", "w") as file:
        for i in lines:
            file.writelines(i)
        file.close()

def printList(lines):
    print("You saved the following to-do items:")
    for i, line in enumerate(lines):
        print("    {}. {}".format(i + 1, line), end = "")

def addToDo():
    item = input("Add an item: ")
    with open("TW1\\todolist.txt", "a") as file:
        file.write("[ ] " + item + "\n")
        file.close()

def markCompleted(lines):
    accepted = False
    row = 0
    while not accepted:
        row = input("Which one you want to mark as completed: ")
        try:
            row = int(row)
            accepted = True
        except:
            print("Please type in a number!")
            accepted = False
    line = str(lines[row - 1])
    if line[1] == " ":
        print(line[4:-1] + " is completed")
        line = list(line)
        line[1] = "x"
        line = "".join(line)
        lines[row - 1] = line
    else:
        print("Already marked completed!")
    return lines

def archive(lines):
    print("All completed tasks got deleted.")
    tmplines = []
    i = 0
    while i < len(lines):
        #print("{} at index {}".format(line, index))
        tmp = list(lines[i])
        if tmp[1] == " ":
            tmp = "".join(tmp)
            tmplines.append(tmp)
        i += 1
    #print(tmplines)
    return tmplines

lines = loadFile()

try:
    if sys.argv[1] == "list":
        printList(lines)
    elif sys.argv[1] == "add":
        addToDo()
    elif sys.argv[1] == "mark":
        lines = markCompleted(lines)
        saveFile(lines)
    elif sys.argv[1] == "archive":
        lines = archive(lines)
        saveFile(lines)
    else:
        print("Please specify a command [list, add, mark, archive]: ", end = "")
except:
    print("Please specify a command [list, add, mark, archive]: ", end = "")

#print(lines)