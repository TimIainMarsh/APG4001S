import numpy as np
import math as mt

gamE = 9.7803267715
k =0.001931851353
e_2= 0.00669438002290


class TrigStations(object):
    def __init__(self,Lat,Long,r,EHeight,GHeight):
        self.Lat = -mt.radians(Lat[0] + Lat[1]/60 + Lat[2]/3600)
        self.Long = mt.radians(Long[0] + Long[1]/60 + Long[2]/3600)
        self.r = mt.sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))
        self.EHeight = EHeight
        self.GHeight = GHeight

Trignetstations ={'HNUS':TrigStations([34,25,28.6671],[19,13,23.0264],[4973168.840,1734085.512,-3585434.051],63.048,32.17),
                  'PRET':TrigStations([25,43,55.2935],[28,16,57.4873],[5064032.237,2724721.031,-2752950.762],1387.339,24.84),
                  'RBAY':TrigStations([28,47,43.9616],[32,4,42.1896],[4739765.776,2970758.460,-3054077.535],31.752,23.54),
                  'TDOU':TrigStations([23,4,47.6714],[30,23,2.4297],[5064840.815,2969624.535,-2485109.939],630.217,13.08),
                  'ULDI':TrigStations([28,17,35.2196],[31,25,15.3309],[4796680.897,2930311.589,-3005435.714],607.947,26.60)}

def height(data):
        OrthHeight= data.EHeight - data.GHeight
        Gamma =gamE * (1+k*(mt.sin(data.Lat)**2))/(mt.sqrt(1-e_2*(mt.sin(data.Lat)**2)))
        N_Gamma = Gamma -0.1543*OrthHeight*(10**-5)
        return OrthHeight * ((Gamma-N_Gamma)/Gamma)
        


if __name__ == "__main__":
    for name,data in Trignetstations.items():
        print(name,height(data))
    






        





















