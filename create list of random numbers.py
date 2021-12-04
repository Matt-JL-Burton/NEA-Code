import random
listOfRandomNumbers = []
for i in range(256):
    randomNumberToAdd = random.randint(2000,10000)
    while randomNumberToAdd in listOfRandomNumbers:
        randomNumberToAdd = random.randint(2000,10000)
    listOfRandomNumbers.append(str(randomNumberToAdd))
print(listOfRandomNumbers)
