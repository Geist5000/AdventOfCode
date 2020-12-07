
class Policy:
    def __init__(self,min,max,character):
        self.min = min
        self.max = max
        self.character = character
    def isValid(self,password):
        count = password.count(self.character)
        return self.min<=count and self.max>=count
    def parse(data):
        polData = data.split(" ")
        character = polData[1]
        minMax = polData[0].split("-")
        return Policy(int(minMax[0]),int(minMax[1]),character)


def isValid(line):
    splitted = line.split(":")
    pol = Policy.parse(splitted[0])
    return pol.isValid(splitted[1])

if __name__ == "__main__":
    lines = []
    with open("data.txt","r") as f:
        lines = list(map(lambda x: x.replace("\n",""),f.readlines()))
        
    count = 0
    for l in lines:
        if(isValid(l)):
            count += 1
    print(count)
    