visited = []
acc = 0

index = 0

def perfAcc(input):
	global acc,index
	acc += int(input)
	index += 1

def perfJmp(input):
	global index
	index += int(input)
	
def perfNop(input):
	global index
	index += 1

operations = []
with open("data.txt", "r") as f:
	operations = list(map(lambda l: l.replace("\n",""),f.readlines()))

while(index not in visited):
	visited.append(index)
	op = operations[index].split(" ")
	instruction = op[0]
	if(instruction=="acc"):
		perfAcc(op[1])
	elif(instruction =="nop"):
		perfNop(op[1])
	elif(instruction == "jmp"):
		perfJmp(op[1])
print(acc)
	
	
