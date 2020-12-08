lines = []

with open("data.txt","r") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
    
    
    
count = 0
groupQuestions = []
for l in lines:
    if(len(groupQuestions) == 0):
        groupQuestions.extend(l)
    if(len(l) == 0):
        count += len(groupQuestions)
        groupQuestions = []
    groupQuestions = [c for c in groupQuestions if c in l]
            
            
count += len(groupQuestions)

print(count)