lines = []

def solve(numbers):
    occurringcies = {}
    index = 1
    for n in numbers[:-1]:
        occurringcies[n] = index
        index+=1


    nextNumber = numbers[-1]
    while(index <2020):
        if(nextNumber in occurringcies):
            diff = index - occurringcies[nextNumber]
            occurringcies[nextNumber] = index
            nextNumber = diff
        else:
            occurringcies[nextNumber] = index
            nextNumber = 0
        index += 1
    return nextNumber

with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n","").split(","),f.readlines()))


for l in lines:
    numbers = list(map(int,l))
    print(solve(numbers))