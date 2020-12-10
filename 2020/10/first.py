lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: int(l.replace("\n","")),f.readlines()))
    
lines.sort()

diff1 = 0
diff3 = 1 # one is always present, because the in device adapter is always 3 away
prev = 0

for n in lines:
    diff = n - prev
    if(diff== 1):
        diff1+= 1
    elif (diff == 3):
        diff3+=1
    else:
        print("Illegal Space Between adapters")
    prev = n
print("1 diff: " + str(diff1))


print("3 diff: " + str(diff3))

print("solution: " + str(diff1*diff3))