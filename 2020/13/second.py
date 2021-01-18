def solve(busIds):
    # list of tuples with (index,id)
    if(len(busIds) > 2):
        prevNumber = solve(busIds[:len(busIds)-1])
        lastNumber = busIds[-1]
        prevIndex = prevNumber[0]
        lastIndex = lastNumber[0]

        lastNumber = (lastIndex - prevIndex,lastNumber[1])
        prevNumber = (0,prevNumber[1])
        busIds = [prevNumber,lastNumber]
    
    m = max(map(lambda x: int(x[1]),busIds))
    currentIndex = 0
    while(True):
        start = None
        for i,id in busIds:
            if(start == None):
                
                current = int(currentIndex*m/id)*id
                start = current
            else:
                diff = id-start%id
                if(diff != i):
                    f = False
                    break
                else:
                    return (i,start+diff)
        currentIndex += 1
        






lines = []


with open("testInput.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))


for l in lines[1:]:

    busIds = l.split(",")
    busIds = list(map(lambda x: (x[0],int(x[1])),filter(lambda x: x[1] != "x", enumerate(busIds))))

    print(solve(busIds))
