needed = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

class Passport:
	def __init__(self):
		self.data = []
	def addData(self,data):
		self.data.extend(list(map(lambda x: x.split(":")[0],data.split(" "))))
	def isValid(self):
		global needed
		return not any(list(map(lambda x: x not in self.data,needed)))
		
	
lines = []	
with open("data.txt","r") as f:
	lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
	
count = 0
passport = Passport()

for l in lines:
	if(len(l)>0):
		passport.addData(l)
	else:
		if(passport.isValid()):
			count += 1
		passport = Passport()
		
		
if(passport.isValid()):
	count += 1
print(count)
		