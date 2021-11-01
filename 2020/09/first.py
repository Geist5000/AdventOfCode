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

for i,number in enumerate(lines):
    if i < preamble:
        continue
    
    offset = i - preamble
    pre = lines[offset:offset + preamble]
    
    if(not canAddUp(pre,number)):
        print(number)
        break
