def parseField(fieldLine):
    parsed = {}
    splitted = fieldLine.split(": ")
    parsed["name"] = splitted[0]
    ranges = splitted[1].split(" or ")
    parsed["ranges"] = ranges

    return parsed

def checkIfInRanges(ranges,value):
    for r in ranges:
        splitted = list(map(int,r.split("-")))
        if(value>= splitted[0] and value <= splitted[1]):
            return True
    return False


lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))

# enthält dicts mit einem name und ranges field. Name ist ein string und und ranges eine liste von strings
fields = []

myTicket = None
nearby = []

invalidNumbers = []

readingFields = True
nextMyTicket = False
nearbyTickets = False
for l in lines:
    
    if(readingFields):
        if(len(l) == 0):
            readingFields = False
            continue
        fields.append(parseField(l))
    elif(nextMyTicket):
        myTicket = list(map(int,l.split(",")))
        nextMyTicket = False
    elif(nearbyTickets):
        current = list(map(int,l.split(",")))
        nearby.append(current)
        for n in current:
            invalid = not any(map(lambda x: checkIfInRanges(x["ranges"],n),fields))
            if(invalid):
                invalidNumbers.append(n)
    elif(l.startswith("your")):
        nextMyTicket = True
    elif(l.startswith("nearby")):
        nearbyTickets = True

print(sum(invalidNumbers))