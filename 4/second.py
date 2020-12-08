import re


eyeColors = ["amb","blu","brn","gry","grn","hzl","oth"]

def checkHeight(x):
	match = re.fullmatch(r'([0-9]+)(cm|in)',x)
	if( match == None):
		return False
	height = int(match.group(1))
	unit = match.group(2)
	if(unit == "in"):
		return height>=59 and height<=76
	if(unit == "cm"):
		return height>= 150 and height<=193

needed = {
	"byr": lambda x: int(x)>=1920 and int(x)<=2002,
	"iyr":lambda x: int(x)>=2010 and int(x)<=2020,
	"eyr":lambda x: int(x)>=2020 and int(x)<=2030,
	"hgt":checkHeight,
	"hcl":lambda x: not re.fullmatch(r'#[0-9a-f]{6}',x) == None,
	"ecl":lambda x: x in eyeColors ,
	"pid":lambda x: not re.fullmatch(r'(\d{9})',x) == None }

class Passport:
	def __init__(self):
		self.data = []
	def addData(self,data):
		self.data.extend(list(map(lambda x: x.split(":"),data.split(" "))))
	def hasValidField(self,field):
		for d in self.data:
			if d[0] == field[0]:
				return field[1](d[1])
		return False
	def isValid(self):
		global needed
		return not any(list(map(lambda x: not self.hasValidField((x,needed[x])),needed)))
		
	
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
		