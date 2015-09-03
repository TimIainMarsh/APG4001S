############################################################
###  Read brdc file for specific satelite and compute
###  ephemiris for rest of orbit (96) every 900s (15min)
###
###  then check this against the sp3 file for the same
###  satelite
###
###  For this assignment i will be using satelite 12
###
# class TrigStations(object):
#     def __init__(self,Lat,Long,r,height):
#         self.Lat = -mt.radians(Lat[0] + Lat[1]/60 + Lat[2]/3600)
#         self.Long = mt.radians(Long[0] + Long[1]/60 + Long[2]/3600)
#         self.r = mt.sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))
#         self.height = height
###
############################################################
from NavMsg import ReadNavMessage



if __name__ == "__main__":
	#step 1: read nav message

	SatPRN = 16
	Sat = ReadNavMessage(SatPRN)
	Epochs = []
	for i,j in Sat.items():
		Epochs.append(i)
	Epochs.sort()

	#step 2 calculate ephemeris

	Epoch = Epochs[0]

	##################

	A = Sat[Epoch].sqrt_A **2


	#step 3: read sp3


	#step 4: compare
