def inputEverything():
    str = input("Please type in the elements separated by spaces! (1 -5 cat): ")
    list = str.split(" ")
    return list

def inputOnlyNumbers():
    accepted = False
    while not accepted:
        str = input("Please type in numbers separated by spaces! (1 5 8): ")
        numbers = str.split(" ")
        try:
            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])
                accepted = True
        except:
            print("Please follow the example!")
            accepted = False
    return numbers

def minNumber(numbers):
    min = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
    return min

def maxNumber(numbers):
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max

def avg(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum / len(numbers)

def searchAndSort(list):
    tmp = []
    for i in list:
        try:
            tmp.append(int(i))
        except:
            pass
            #print("Couldn't convert that one!")
    return tmp

defList = inputEverything()
print(defList)
defList = searchAndSort(defList)
print(defList)
print("The minimum number is: {}".format(minNumber(defList)))
print("The maximum number is: {}".format(maxNumber(defList)))
print("The average is: {}".format(avg(defList)))