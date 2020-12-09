lines = []

with open("data.txt","r") as f:
	lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
	
	
def getPlace(x,y):
	global lines
	l = lines[y%len(lines)]
	return l[x%len(l)]
	
	
x = 0
y = 0
counter = 0

# xOffset = 3
# xOffset = 1
# xOffset = 5
# xOffset = 7
xOffset = 1
yOffset = 2


while(y < len(lines)-1):
	if(getPlace(x,y) == "#"):
		counter += 1
	x += xOffset
	y += yOffset
	
print(counter)