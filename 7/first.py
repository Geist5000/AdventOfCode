# {name} bags contain {number} {name} bags, .
# {name} bags contain no other bags.
# {name} bags contain {number} {name} bags, {number} {name} bags.

class Bag:

    def __init__(self,name,canContain = []):
        self.name = name
        self.canContain = canContain
        
        
    def doesContain(self, bag):
        if any(list(map(lambda x: x[1].name == bag.name,self.canContain))):
            return True
        else:
            for b in self.canContain:
                if(b[1].doesContain(bag)):
                    return True   
            return False
    def count(self):
        sum = 0
        for b in self.canContain:
            sum += b[0] + b[0] * b[1].count()
        return sum
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
            
def getEmptyBagsAndRemove(bagLines):
    result =[]
    for b in bagLines:
        if(b[1] == "no other bags."):
            result.append(b)
            
            
    for r in result:
        bagLines.remove(r)
    return result
    
    
def getBagsWhichAreHold(bagLine):
    containing = bagLine[1].split(", ")
    result = []
    for c in containing:
        indexOfSpace = c.index(" ")
        numberOfbags = int(c[:indexOfSpace])
        indexOfBags = c.index(" bag")
        result.append((numberOfbags,c[indexOfSpace+1:indexOfBags]))
    return result
        
    
def getBagWithName(bags,bagName):
    for b in bags:
        if(b.name == bagName):
            return b
            
    return None
    
if __name__ == "__main__":
    lines = []
    bags = []
    with open("data.txt","r") as f:
        lines = list(map(lambda x: x.replace("\n","").split(" bags contain ") ,f.readlines()))
    
    for b in getEmptyBagsAndRemove(lines):
        bags.append(Bag(b[0]))
        
    while(len(lines)>0):
        toRemove = []
        for l in lines:
            contains = getBagsWhichAreHold(l)
            containedBags = list(map(lambda x: (x[0],getBagWithName(bags,x[1])),contains))
            allfound = not any(list(map(lambda x: x[1]==None,containedBags)))
            if(allfound):
                bags.append(Bag(l[0],containedBags))
                toRemove.append(l)
        
        for tr in toRemove:
            lines.remove(tr)
            
            
    toSearch = getBagWithName(bags,"shiny gold")
    
    count = 0
    for b in bags:
        if(b.doesContain(toSearch)):
            count+=1
            
    print("First task:")
    print(count)
    
    print("Second task:")
    print(toSearch.count())
    
   
    

