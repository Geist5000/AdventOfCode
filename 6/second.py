lines = []

with open("data.txt","r") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
    
    
    
count = 0
groupQuestions = None
for l in lines:
    
    if(len(l) == 0):
        count += len(groupQuestions)
        groupQuestions = None
    else:
        if(groupQuestions == None):
            groupQuestions = l
        else:
            groupQuestions = [c for c in groupQuestions if c in l]
            
            
if(groupQuestions != None):
    count += len(groupQuestions)

print(count)