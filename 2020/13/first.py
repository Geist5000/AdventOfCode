lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))


startTime = int(lines[0])
busIds = lines[1].split(",")

smallestDiff = None
smallestId = -1
for id in busIds:
    if id != "x":
        time = int(id)
        diff =time - startTime%time
        if(smallestDiff == None or smallestDiff> diff):
            smallestDiff = diff
            smallestId = time
print(smallestDiff*smallestId)