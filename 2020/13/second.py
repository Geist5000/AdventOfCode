def solve(busIds):
    # list of tuples with (index,id)#

    if(len(busIds) == 2):
        return findMatches(busIds)
    else:
        prevMatches = solve(busIds[:-1])
        diff = prevMatches[1]-prevMatches[0]

        matches = []
        index =1
        while(len(matches)<2):
            res =prevMatches[0]+index*diff
            match = checkIfMatch(busIds,res)
            if(match):
                matches.append(res)
            index += 1
        return matches
    

    


def findMatches(numbers,count = 2):
    # list with two values which are (index,id)
    bigger = max(numbers,key=lambda x: x[1])
    matches = []
    index = 1
    while(len(matches) < count):
        res = index * bigger[1]-bigger[0]
        match = checkIfMatch(numbers,res)
        if(match):
            matches.append(res)
        index += 1
    return matches

def checkIfMatch(constraints,value):
    return all(map(lambda x: (value+x[0])%x[1] == 0,constraints))

        






lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))


for l in lines[1:]:

    busIds = l.split(",")

    # converts the input string (1,x,5,8,x,9) into a list of tuples
    #  which have the index of the number as first value and the number itself as second value
    busIds = list(map(lambda x: (x[0],int(x[1])),filter(lambda x: x[1] != "x", enumerate(busIds))))

    print(solve(busIds)[0])
