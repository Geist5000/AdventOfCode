lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: int(l.replace("\n","")),f.readlines()))

result = 0
for l in lines:
    result += l
print(result)
