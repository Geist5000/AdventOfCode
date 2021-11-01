lines = []


preamble = 25

with open("data.txt") as f:
    lines = list(map(lambda l: int(l.replace("\n","")),f.readlines()))
    
def canAddUp(numbers,number):
    for i,n in enumerate(numbers[:len(numbers)-1]):
        if(n>number):
            continue
        for n2 in numbers[i+1:]:
            if(n2+n == number):
                return True
    return False
    
def calcContiousSet(numbers,goal):
    for i,n in enumerate(numbers[:len(numbers)-1]):
        sum = n
        for j,n2 in enumerate(numbers[i+1:],i+1):
            sum += n2
            if(goal < sum):
                break
            if(goal == sum):
                return numbers[i:j+1]
                
    return []
                
    
    
    
    

for i,number in enumerate(lines):
    if i < preamble:
        continue
    
    offset = i - preamble
    pre = lines[offset:offset + preamble]
    
    if(not canAddUp(pre,number)):
        print(number)
        continous = sorted(calcContiousSet(lines[:i+1],number))
        print(continous[0] + continous[-1])
        break
