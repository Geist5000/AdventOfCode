lines = []

with open("data.txt","r") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
    
    
    
count = 0
groupQuestions = []
for l in lines:
    if(len(l) == 0):
        count += len(groupQuestions)
        groupQuestions = []
    for c in l:
        if c not in groupQuestions:
            groupQuestions.append(c)
            
            
count += len(groupQuestions)
groupQuestions = []

print(count)