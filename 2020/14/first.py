import re


class ChallengeHandler:
    def __init__(self) -> None:
        self.mask = "X"*36
        self.memory = {}

    def handleMaskChange(self,newMask) -> None:
        self.mask = newMask

    def saveValue(self,index,value) -> None:
        processedValue = self.applyMaskToValue(value)
        self.memory[index] = processedValue


    def applyMaskToValue(self,value) -> int:
        newValue = value|int(self.getOrMask(),2)
        newValue = newValue&int(self.getAndMask(),2)
        return newValue

    def getOrMask(self) -> str:
        return self.mask.replace("X","0")
    def getAndMask(self) -> str:
        return self.mask.replace("X","1")
    def getSumOfValues(self) -> int:
        return sum(self.memory.values())

lines = []

lineRegex = r'(mask|mem\[([0-9]+)\]) = ([0-9]+|[X01]+)'


with open("data.txt") as f:
    lines = list(map(lambda l: re.fullmatch(lineRegex, l.replace("\n","")),f.readlines()))


challenge = ChallengeHandler()
for l in lines:
    instruction = l.group(1)
    if(instruction.startswith("mem")):
        challenge.saveValue(int(l.group(2)),int(l.group(3)))
    elif(instruction.startswith("mask")):
        challenge.handleMaskChange(l.group(3))
    else:
        raise Exception("wrong instruction")

print(challenge.getSumOfValues())


