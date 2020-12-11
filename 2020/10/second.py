def howManyCanSkip(numbers):
    start = numbers[0]
    count = 0
    for n in numbers[2:]:
        diff = abs(n- start)
        if(diff < 4):
            count += 1
        else:
            break
            
    return count
        


lines = []


with open("testInput.txt") as f:
    lines = list(map(lambda l: int(l.replace("\n","")),f.readlines()))

lines.append(0)
lines.sort()

# lines = [1,2,3,4]

print(lines)

combinations = 1


previouslySkippable = 0
alreadySkipped = 0
skip = False
for i,n in enumerate(lines):
    if(i < len(lines)-2):
        if(skip):
            skip = False
            continue
        skippable = howManyCanSkip(lines[i:])
        combs = pow(2,skippable)
        
        if(skippable>0):            
            if(previouslySkippable== 0):
                combinations *= combs
            if(previouslySkippable == 1 and skippable>0):
                combinations *= combs
                combinations -= 1
            if(previouslySkippable == 2 and skippable==2):
                combinations *= combs
                
        if(skippable == 2):
            skip = True
        
        previouslySkippable = skippable
        

print("Possible combs: " + str(combinations))