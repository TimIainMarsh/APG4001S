def FixValue(num):
	if len(num) == 0: return 0
	number = num.split("D")
	return float(number[0]) * 10**(float(number[1]))


class SatNavMsg(object):
	def __init__(self):
		self.PRN = None
		# self.PRN = None
		# self.Epoch = None
		# self.SVclockbias = None
		# self.SVclockbrift = None
		# self.SVclockdriftrate = None
		# self.PRN = None
		# self.Epoch = None
		# self.SVclockbias = None
		# self.SVclockbrift = None
		# self.SVclockdriftrate = None
		# self.IODE = None
		# self.Crs = None
		# self.DeltaN = None
		# self.M0 = None
		# self.Cuc = None
		# self.e = None
		# self.Cus = None
		# self.sqrtA = None
		# self.Toe = None
		# self.Cic = None
		# self.OMEGA = None
		# self.CIS = None
		# self.i0 = None
		# self.Crc = None
		# self.omega = None
		# self.OMEGADOT = None
		# self.IDOT = None
		# self.L2Code = None
		# self.GPSWeek = None
		# self.L2PdataFlag = None
		# self.SVaccuracy = None
		# self.SVhealth = None
		# self.TGD = None
		# self.IODC = None
		# self.TransTime = None
		# self.FitIntervle = None
		# self.spare = None
		# self.spare2 = None

	def setLineData(self,_1,_2,_3,_4,_5):
		self.PRN = _1
		self.Epoch = _2
		self.SVclockbias = FixValue(_3)
		self.SVclockbrift = FixValue(_4)
		self.SVclockdriftrate = FixValue(_5)

	def setLine1(self,_1,_2,_3,_4):
		self.IODE = FixValue(_1)
		self.Crs = FixValue(_2)
		self.DeltaN = FixValue(_3)
		self.M0 = FixValue(_4)

	def setLine2(self,_1,_2,_3,_4):
		self.Cuc = FixValue(_1)
		self.e = FixValue(_2)
		self.Cus = FixValue(_3)
		self.sqrtA = FixValue(_4)

	def setLine3(self,_1,_2,_3,_4):
		self.Toe = FixValue(_1)
		self.Cic = FixValue(_2)
		self.OMEGA = FixValue(_3)
		self.Cis = FixValue(_4)

	def setLine4(self,_1,_2,_3,_4):
		self.i0 = FixValue(_1)
		self.Crc = FixValue(_2)
		self.omega = FixValue(_3)
		self.OMEGADOT = FixValue(_4)

	def setLine5(self,_1,_2,_3,_4):
		self.IDOT = FixValue(_1)
		self.L2Code = FixValue(_2)
		self.GPSWeek = FixValue(_3)
		self.L2PdataFlag = FixValue(_4)

	def setLine6(self,_1,_2,_3,_4):
		self.SVaccuracy = FixValue(_1)
		self.SVhealth = FixValue(_2)
		self.TGD = FixValue(_3)
		self.IODC = FixValue(_4)

	def setLine7(self,_1,_2,_3,_4):
		self.TransTime = FixValue(_1)
		self.FitIntervle = FixValue(_2)
		self.spare = FixValue(_3)
		self.spare2 = FixValue(_4)





class SatNavMsgDict(dict):
	def __init__(self,PRN):
		self.PRN = PRN



def ReadFile(filename):
	lines = []
	f = open(filename, 'r')
	for line in f:
		#get lines and strip \n of the end
		lines.append(line[:len(line)-1])
	return lines

def splitLine(line):
	#dont fuck with this function
	_1 = line[3:22]
	# print(_1)
	_2 = line[22:41]
	# print(_2)
	_3 = line[41:60]
	# print(_3)
	_4 = line[60:]
	# print(_4)
	return [_1,_2,_3,_4]

def splitDataLine(line):
	#dont fuck with this function
	_1 = line[:3]
	line = line[3:]
	_2 = line[:3]
	line = line[3:]
	_3 = line[:3]
	line = line[3:]
	_4 = line[:3]
	line = line[3:]
	_5 = line[:3]
	line = line[3:]
	_6 = line[:3]
	line = line[3:]

	_7 = line[:4]
	line = line[4:]

	_8 = line[:19]
	line = line[19:]
	_9 = line[:19]
	line = line[19:]
	_10 = line[:19]
	line = line[19:]

	return [_1,_2,_3,_4,_5,_6,_7,_8,_9,_10]

def ReadNavMessage(PRN):
	lines = ReadFile("NAVandSP3/brdc2000.15n")
	count = -1

	Sat = SatNavMsgDict(PRN)

	Sat_data = SatNavMsg()

	for i in lines:
		count +=1

		if i[:2] == str(PRN):
			Sat_data = SatNavMsg()
			### LINE D ###
			lineD = splitDataLine(lines[count])
			Epoch = [float(lineD[1]),float(lineD[2]),float(lineD[3]),float(lineD[4]),float(lineD[5]),float(lineD[6])]
			Sat_data.setLineData(lineD[0],Epoch,lineD[7],lineD[8],lineD[9])

			### LINE1 ###
			line1 = splitLine(lines[count+1])
			Sat_data.setLine1(line1[0],line1[1],line1[2],line1[3])

			### LINE2 ###
			line2 = splitLine(lines[count+2])
			Sat_data.setLine2(line2[0],line2[1],line2[2],line2[3])

			### LINE3 ###
			line3 = splitLine(lines[count+3])
			Sat_data.setLine3(line3[0],line3[1],line3[2],line3[3])

			### LINE4 ###

			line4 = splitLine(lines[count+4])
			Sat_data.setLine4(line4[0],line4[1],line4[2],line4[3])

			### LINE5 ###

			line5 = splitLine(lines[count+5])
			Sat_data.setLine5(line5[0],line5[1],line5[2],line5[3])

			### LINE6 ###

			line6 = splitLine(lines[count+6])
			Sat_data.setLine6(line6[0],line6[1],line6[2],line6[3])

			### LINE7 ##
			line7 = splitLine(lines[count+7])
			Sat_data.setLine6(line7[0],line7[1],line7[2],line7[3])

			name = str(lineD[4].strip())+"-"+str(lineD[5].strip())+"-"+str((lineD[6].strip())[:-2])
			Sat[name] = Sat_data

	return Sat