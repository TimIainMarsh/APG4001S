class GGM02S_File_Save(dict):
    def __init__(self,line1,line2):
        self.info1 = line1
        self.info2 = line2

class GGM02SLine(object):
    def __init__(self,CS,coeff,m,n,value):
        self.CS = CS
        self.m = int(m)
        self.n = int(n)
        self.coeff = coeff
        value = value.replace('\n','')
        ans = value.split('D')
        value = float(ans[0]) * (10 ** float(ans[1]))
        self.value = value

def readFile(filename):
	lines = []
	f = open(filename, 'r')
	for line in f:
		lines.append(line)
	return lines

def organizeLines(linesFile):
	ggm02s = GGM02S_File_Save(linesFile[0],linesFile[1])
	linesFile.pop(0)
	linesFile.pop(0)
	#coeff  m  n  value
	for line in linesFile:

		coeff = line[0:7]
		line = line[7:]
		line = line.replace('       ','')
		m = line[0:3]
		line = line[3:]
		n = line[0:3]
		line = line[3:]
		line = line.lstrip()
		value = line

		ggm02s[str(coeff[5:6])+' '+str(m).lstrip()+' '+str(n).lstrip() ] = GGM02SLine(coeff[5:6],coeff,m,n,value)
		# print(len(dictionary))

	return ggm02s

