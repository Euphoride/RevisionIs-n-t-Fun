import random
import time

def printStuff1(foo, bar):
    DisplayText = "What is the proper term for \"" + foo[:-1] + "\"?"

    print("----------------------------------------------------------------")
    print(DisplayText)
    print("----------------------------------------------------------------")
    input()

    print("Answer was: " + bar)
    yn = input("Did you get it right? (Y/N)")
    print("")

    if yn in ["y", "Y"]:
        currentWentBy = wentBy[holderForX] - 1

        tempHolderForWeight = weights[holderForX]

        weights[holderForX] = weights[holderForX] - (weights[holderForX] * (1/currentWentBy))

        difference = tempHolderForWeight - weights[holderForX]

        for x in range(len(weights)):
            if weights[holderForX] != weights[x]:
                weights[x] = weights[x] - (difference / (len(weights) - 1))

    else:
        currentWentBy = wentBy[holderForX] + 1

        tempHolderForWeight = weights[holderForX]

        weights[holderForX] = weights[holderForX] - (weights[holderForX] * (1/currentWentBy))

        difference = tempHolderForWeight - weights[holderForX]

        for x in range(len(weights)):
            if weights[holderForX] != weights[x]:
                weights[x] = weights[x] - (difference / (len(weights) - 1))

    return "bloop"

def printStuff2(foo, bar):
    DisplayText = "What does the term \"" + foo[:-1] + "\" mean?"

    print("----------------------------------------------------------------")
    print(DisplayText)
    print("----------------------------------------------------------------")
    input()

    print("Answer was: " + bar)
    yn = input("Did you get it right? (Y/N)")
    print("")

    if yn in ["y", "Y"]:
        currentWentBy = wentBy[holderForX] - 1

        tempHolderForWeight = weights[holderForX]

        weights[holderForX] = weights[holderForX] - (weights[holderForX] * (1/currentWentBy))

        difference = tempHolderForWeight - weights[holderForX]

        for x in range(len(weights)):
            if weights[holderForX] != weights[x]:
                weights[x] = weights[x] - (difference / (len(weights) - 1))

    else:
        currentWentBy = wentBy[holderForX] + 1

        tempHolderForWeight = weights[holderForX]

        weights[holderForX] = weights[holderForX] - (weights[holderForX] * (1/currentWentBy))

        difference = tempHolderForWeight - weights[holderForX]

        for x in range(len(weights)):
            if weights[holderForX] != weights[x]:
                weights[x] = weights[x] - (difference / (len(weights) - 1))

    return "bloop"


inputFileHandler1 = open("names.txt", 'r')
inputFileHandler2 = open("texts.txt", 'r')

names = inputFileHandler1.readlines()
texts = inputFileHandler2.readlines()

weights = []

wentBy = []

for x in range(len(names)):
    weights.append(len(names) / 100)
    wentBy.append(8)

while True:

    unodos = random.randint(1,2)

    holderForX = 0

    if unodos == 1:
        values = []

        lastWeight = 0
        for weight in weights:
            values.append(lastWeight + (weight))
            lastWeight += weight


        fooN = random.randint(0, 100)


        for x in range(len(values)):
            if fooN > values[x]:
                continue
            elif fooN == values[x]:
                foo = texts[x]
                bar = names[x]
                holderForX = x
                printStuff1(foo, bar)
                break
            elif fooN < values[x]:
                foo = texts[x - 1]
                bar = names[x - 1]
                holderForX = x - 1
                printStuff1(foo, bar)
                break

    else:
        values = []

        lastWeight = 0
        for weight in weights:
            values.append(lastWeight + (weight))
            lastWeight += weight


        fooN = random.randint(0, 100)


        for x in range(len(values)):
            if fooN > values[x]:
                continue
            elif fooN == values[x]:
                foo = names[x]
                bar = texts[x]
                holderForX = x
                printStuff2(foo, bar)
                break
            elif fooN < values[x]:
                foo = names[x - 1]
                bar = texts[x - 1]
                holderForX = x - 1
                printStuff2(foo, bar)
                break
