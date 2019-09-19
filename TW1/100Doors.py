doors = []
for i in range(100):
    doors.append(0)
#print(len(doors))

i = 1
while i <= len(doors):
    for k in range(i - 1, len(doors), i):
        if doors[k] == 1:
            doors[k] = 0
        else:
            doors[k] = 1
    i += 1
    print(doors)
print(i)

print("The following doors are open: ", end="")
for index, door in enumerate(doors):
    if door == 1:
        print("{}, ".format(index + 1), end="")