import ReadWrite as RW
import math as mt
from scipy import special as SCSP
import sympy

class TrigStations(object):
    def __init__(self,Lat,Long,r,LoBand):
        self.Lat = mt.radians(Lat[0] + Lat[1]/60 + Lat[2]/3600)

        self.Long = mt.radians(Long[0] + Long[1]/60 + Long[2]/3600)
        self.r = mt.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
        self.LoBand = LoBand
        
def get_N(data):
    cos = mt.cos
    sin = mt.sin
    sqrt = mt.sqrt

    a  = 6378137
    GM = 3986005*10**8
    J_20 = 108263*10**-8
    gamE = 9.7803267715
    k = 0.001931851353
    e2 = 0.00669438002290

    gam = gamE * ((1 + k*sin(data.Lat)**2)/(sqrt(1- e2 * sin(data.Lat)**2)))

    first = GM / gam * data.r

    outerSum = 0
    for n in range(2,10):

        innerSum = 0

        for m in range(0,n):
            queryC = 'C '+str(n)+' '+str(m)
            Cnm = float(ggm02s[queryC].value)

            if m == 0:
                continue
            queryS = 'S '+str(n)+' '+str(m)
            Snm = float(ggm02s[queryS].value)
            dCnm = Cnm #+ J_20

            
            pnm = round(sympy.assoc_legendre(n,m,mt.cos(data.Lat)),5)
            # print (pnm)
            val = (dCnm * cos(m * data.Long) + Snm * sin(m * data.Long))*pnm

            innerSum += val

        outerSum += ((a/data.r)**n) * innerSum
    N = first * outerSum
    return N


if __name__ == '__main__':


    linesFile = RW.readFile('grvfld.ggm02s')
    ggm02s = RW.organizeLines(linesFile)



    TrignetStations= {'HNUS': TrigStations([34,25,28.6671],[19,13,23.0264],[4973168.840,1734085.512,-3585434.051],19),
                      'PRET': TrigStations([25,43,55.2935],[28,16,57.4873],[5064032.237,2724721.031,-2752950.762],29),
                      'RBAY': TrigStations([28,47,43.9616],[32,4,42.1896], [4739765.776,2970758.460,-3054077.535],33),
                      'TDOU': TrigStations([23,4,47.6714], [30,23,2.4297],  [5064840.815,2969624.535,-2485109.939],31),
                      'ULDI': TrigStations([28,17,35.2196],[31,25,15.3309],[4796680.897,2930311.589,-3005435.714],31)}

    for name,data in TrignetStations.items():
        print (name, get_N(data))





