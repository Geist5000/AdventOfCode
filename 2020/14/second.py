from os import stat
import re

def allIndiciesOf(pattern,searchString:str):
    indicies = []
    
    try:
        foundAt = -1
        while(True):
            foundAt = searchString.index(pattern,foundAt+1)
            indicies.append(foundAt)
    except ValueError:
        return indicies

def setCharOfString(string, toInsert, index):
    newString = string[:index] + toInsert
    if(len(string) -1 > index):
         newString += string[index +1:]

    return newString




class ChallengeHandler:
    def __init__(self) -> None:
        self.mask = "X"*36
        self.memory = {}

    def handleMaskChange(self,newMask) -> None:
        self.mask = newMask

    def saveValue(self,index,value) -> None:
        indexNumber = self.applyMaskToValue(index)
        processedIndexes = self.getAllIndexes(indexNumber)
        for index in processedIndexes:
            self.memory[index] = value


    def applyMaskToValue(self,value) -> int:
        # 0 unchanged | 1 will be overriten | X floating -> ignored in this function
        newValue = value|int(self.getOrMask(),2)
        return newValue

    def getAllIndexes(self,indexNumber):
        indicies = []
        binaryIndex = bin(indexNumber)[2:]
        floatinIndicies = list(map(lambda x: len(binaryIndex)-(x+1),allIndiciesOf("X",list(reversed(self.mask)))))

        for i in range(2**len(floatinIndicies)):
            states = bin(i)[2:]
            states = (len(floatinIndicies)- len(states))*"0" + states
            toAdd = binaryIndex
            for index,m in enumerate(floatinIndicies):
                 toAdd = setCharOfString(toAdd,states[index],m)
            indicies.append(int(toAdd,2))

        return indicies

    def getOrMask(self) -> str:
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


