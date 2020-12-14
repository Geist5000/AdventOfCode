lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))


for l in lines[1:]:

    busIds = l.split(",")

    m = max(map(int,filter(lambda x: x != "x",busIds)))

    found = False
    currentIndex = 0
    while(not found):
        start = None
        f = False
        for i,id in enumerate(busIds):
            if id != "x":
                time = int(id)
                if(start == None):
                    
                    current = int(currentIndex*m/time)*time
                    start = current
                else:
                    diff = time-start%time
                    if(diff != i):
                        f = False
                        break
                    else:
                        f = True
        if(f):
            found = True
            print(start)
            break
        currentIndex += 1
