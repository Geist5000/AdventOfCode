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


def getCombinationsOf(numbers):
    
    if(len(numbers) == 3):
        return [numbers,[numbers[0],numbers[2]]]
    elif(len(numbers) < 3):
        return [numbers]
    else:
        currentNumber = numbers[-1]
        combOfPrev = getCombinationsOf(numbers[:-1])
        result = []
        for c in combOfPrev:
            result.append([*c,currentNumber])
            if(c[-1] - c[-2] < 3):
                result.append([*c[:-1],currentNumber])
        return result
    

        


lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: int(l.replace("\n","")),f.readlines()))

lines.append(0)
lines.sort()
lines.append(lines[len(lines)-1]+3)

# lines = [1,2,3,4]

print(lines)


combCount = 1

prevNumber = 0

lastGroup = [0]
for i,l in enumerate(lines[1:]):
    diff = l-prevNumber
    prevNumber = l
    if(diff == 3):
        combs = getCombinationsOf(lastGroup)
        combCount *= len(combs)
        lastGroup = [l]
    elif(diff == 1):
        lastGroup.append(l)
    else:
        raise Exception()

print("combs: " + str(combCount))