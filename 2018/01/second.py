import itertools


lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: int(l.replace("\n","")),f.readlines()))

resultSet = set([0])
result = 0
for l in itertools.cycle(lines):
    result += l
    if result in resultSet:
        break
    else:
        resultSet.add(result)
print(result)
