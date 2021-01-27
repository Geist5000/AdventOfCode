from typing import Tuple


class Dimension:
    def __init__(self) -> None:
        self.currentDim = {}
        self.nextDim = {}

    def simulate(self):
        # write new state in nextDim (with setCubeState) and then copy nextDim in currentDim
        disabledNeighbours = set()
        for x in self.currentDim.items():
            for y in x[1].items():
                for z in y[1].items():
                    # every active cube
                    neighbours = self.getNeighbours(x[0],y[0],z[0])
                    active = self.getActiveFromNeighbours(neighbours)
                    notActive = [a for a in neighbours if a not in active]
                    disabledNeighbours.update(notActive)
                    activeNeighboursCount = len(active)
                    self.setCubeState(x[0],y[0],z[0],activeNeighboursCount == 2 or activeNeighboursCount == 3)
        for n in disabledNeighbours:
            count = len(self.getActiveNeighbours(n[0],n[1],n[2]))
            self.setCubeState(n[0],n[1],n[2],count == 3)

        self.applyChanges()            


    def getNeighbours(self,x,y,z):
        neighbours = []
        for xOff in range(-1,2):
            for yOff in range(-1,2):
                for zOff in range(-1,2):
                    if(not (xOff == yOff and zOff == yOff and zOff == 0)):
                        nx = x+xOff
                        ny = y+yOff
                        nz = z+zOff
                        neighbours.append((nx,ny,nz))
        return neighbours

    def getActiveNeighbours(self,x,y,z):
        return self.getActiveFromNeighbours(self.getNeighbours(x,y,z))


    def getActiveFromNeighbours(self,neighbours) -> int:
        return [a for a in neighbours if self.getCubeState(a[0],a[1],a[2])]

    def countActiveCubes(self):
        count = 0
        for x in self.currentDim.items():
            for y in x[1].items():
                for z in y[1].items():
                    count += 1
        return count
                        

    def setCubeState(self,x,y,z,state):
        if(x not in self.nextDim):
            self.nextDim[x] = {}
        if(y not in self.nextDim[x]):
            self.nextDim[x][y] = {}
        if(state):
            self.nextDim[x][y][z] = True
        elif(z in self.nextDim[x][y]):
            del(self.nextDim[x][y][z])

    def getCubeState(self,x,y,z) -> bool:
        if(x in self.currentDim):
            if(y in self.currentDim[x]):
                if(z in self.currentDim[x][y]):
                    return True
        return False
    def applyChanges(self):
        self.currentDim = self.nextDim
        self.nextDim = {}


lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
# six cycles to boot up

d = Dimension()
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if(c == "#"):
            d.setCubeState(x,y,0,True)
d.applyChanges()

for round in range(6):
    d.simulate()

print(d.countActiveCubes())


