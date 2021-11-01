def flipNop(l):
	return l.replace("nop","jmp")
def flipJmp(l):
	return l.replace("jmp","nop")
	



class Program:

	def __init__(self):
		self.visited = []
		self.acc = 0
		self.index = 0

	def perfAcc(self,input):
		self.acc += int(input)
		self.index += 1

	def perfJmp(self,input):
		self.index += int(input)
		
	def perfNop(self,input):
		self.index += 1
		
	def run(self,operations):
		while(self.index not in self.visited):
			self.visited.append(self.index)
			op = operations[self.index].split(" ")
			instruction = op[0]
			if(instruction=="acc"):
				self.perfAcc(op[1])
			elif(instruction =="nop"):
				self.perfNop(op[1])
			elif(instruction == "jmp"):
				self.perfJmp(op[1])
			if(self.index == len(operations)):
				return 1
		return 0
		


if __name__ == "__main__":
	operations = []
	with open("data.txt", "r") as f:
		operations = list(map(lambda l: l.replace("\n",""),f.readlines()))
		
	for i,o in enumerate(operations):
		if(o.startswith("jmp")):
			operations[i] = flipJmp(o)
		if(o.startswith("nop")):
			operations[i] = flipNop(o)
		p = Program()
		if(p.run(operations) == 1):
			print(p.acc)
			break;
		operations[i] = o


	
	
