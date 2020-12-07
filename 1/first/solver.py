import time


start = time.time()
f = open("data.txt" , "r")


numbers = list(map(lambda x:int( x.replace("\n","")) ,f))

smallestNumber = 2020

accesses = 0


for number in numbers:
    accesses += 1
    if(number < smallestNumber):
        smallestNumber = number
        
accesses + len(numbers)

numbers = [x for x in  numbers if x + smallestNumber<=2020]


result = 0
for (i,number) in enumerate(numbers):
    accesses += 1
    if(result == 0):
        for secondNumber in numbers[i+1:]:
            accesses += 1
            if(number+secondNumber==2020):
                result = number*secondNumber
                break;
    else:
        break;
print(result)
print(accesses)

print(time.time() - start)