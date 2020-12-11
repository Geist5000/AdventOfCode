class Map:
    def __init__(self,data):
        self.map = {}
        for i,l in enumerate(data):
            self.height = i+1
            for j,c in enumerate(l):
                if(j not in self.map.keys()):
                    self.map[j] = {}
                self.map[j][i] = c
                self.width = j+1
        


    def getPlace(self,x,y):
        return self.map[x][y]

    def setSeat(self,x,y,seat):
        self.map[x][y] = seat
    def getNeighbours(self,x,y):
        neighbours = []
        for nx in range(x-1,x+2):
            if(nx>=0 and nx<self.width):
                for ny in range(y-1,y+2):
                    if(ny>=0 and ny<self.height):
                        if(not (ny == y and nx == x)):
                            neighbours.append(self.getPlace(nx,ny))
        return neighbours
    
    def doIteration(self):
        changes = []
        for x,l in enumerate(self.map.values()):
            for y,s in enumerate(l.values()):
                if(s != "."):
                    neighbours = self.getNeighbours(x,y)
                    count = getOccupiedCount(neighbours)
                    if(count==0):
                        if(s == "L"):
                            changes.append((x,y,"#"))
                            
                    if(count >=4):
                        if(s == "#"):
                            changes.append((x,y,"L"))
        self.applyChanges(changes)
        return len(changes)

    def applyChanges(self,toChange):
        for c in toChange:
            self.setSeat(c[0],c[1],c[2])

    def countOccupied(self):
        count = 0
        for l in self.map.values():
            for s in l.values():
                if(s == "#"):
                    count += 1
        return count
                            


def getOccupiedCount(seats):
    count = 0
    for s in seats:
        if(s == "#"):
            count +=1
    return count

            


lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))


m = Map(lines)

while(m.doIteration() > 0):
    pass


print(m.countOccupied())