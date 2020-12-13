import re
def changeDirection(facingDir,angle):
	# Does work for all mutliples of 90 degrees
	# does return a copy of the facingDir
	# east = (1,0); south = 0,-1; west = (-1,0) nord = (0,1);
	rounds = abs(int(angle/90))
	x = facingDir[0]
	y = facingDir[1]
	print("--" + str(rounds))
	for i in range(rounds):
		print(angle,x,y)
		if(angle<0):
			y *= -1
			
		else:
			x *= -1
		copy = x
		x = y
		y = copy
	return (x,y)
			
	

regex = r'(N|S|E|W|L|R|F)([0-9]+)'
lines = []

coord = (0,0)

facing = (1,0)

with open("data.txt") as f:
    lines = list(map(lambda l: re.fullmatch(regex,l.replace("\n","")),f.readlines()))
	
for c in lines:
	action = c.group(1)
	number = int(c.group(2))
	if action == "L":
		facing = changeDirection(facing,-number)
	elif action == "R":
		facing = changeDirection(facing,number)
	elif action == "F":
		coord = (coord[0] + facing[0]*number,coord[1] + facing[1]*number)
	elif action == "N":
		coord = (coord[0],coord[1] + number)
	elif action == "S":
		coord = (coord[0], coord[1] - number)
	elif action == "E":
		coord = (coord[0] + number,coord[1])
	elif action == "W":
		coord = (coord[0] - number,coord[1])
	else:
		print("Not found: " + action)
print(coord)
print(abs(coord[0])+abs(coord[1]))
		