


def decode(data):
	row = 0
	seat = 0
	currentRow = 128/2
	currentSeat = 8/2
	for c in data:
		if(c == "B"):
			row += currentRow
			currentRow /= 2
		if(c == "F"):
			currentRow /= 2
		if(c == "L"):
			currentSeat /= 2
		if(c == "R"):
			seat += currentSeat
			currentSeat /= 2
	return (int(row),int(seat))
	
highest = 0

lines = []

with open("data.txt","r") as f:
	lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
		
		
seats = []
for l in lines:
	seat = decode(l)
	current = seat[0]*8 + seat[1]
	seats.append(current)
	if(current> highest):
		highest = current


for r in range(128):
	for s in range(8):
		current = r*8 + s
		if( current not in seats):
			print(str(r) + "," + str(s) + ": " + str(current)) ## the one in the middle is the searched seat
			
print(highest)