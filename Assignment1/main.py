import ReadWrite as RW
import math as mt
import numpy as np
# from scipy import special as SCS
import sympy

class TrigStations(object):
    def __init__(self,Lat,Long,r):
        self.Lat = -mt.radians(Lat[0] + Lat[1]/60 + Lat[2]/3600)
        self.Long = mt.radians(Long[0] + Long[1]/60 + Long[2]/3600)
        self.r = mt.sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))

def get_p(n, m, t):
    r = (n - m) / 2
    modr = (n-m)%2
    if modr != 0:
        r = (n - m - 1)/2
    Sum = 0.0
    for k in range (0, int(r)+1):
        a = (-1)**k
        b = (n - m - 2*k)
        c = mt.factorial(2*n - 2*k)
        d = mt.factorial(k)
        f = mt.factorial(n - k)
        g = mt.factorial(n - m - 2*k) 
        h = t ** (n - m -2*k)
        this_loop = a* (c/(d*f*g))*h
        Sum += this_loop
    return (2 ** (-n) * (1 - t ** 2) ** (m/2.0)) * Sum

def get_normilized_p(n, m, t):
    p = get_p(n,m,t)
    # p = sympy.assoc_legendre(n, m, t)
    if m == 0:
        j = 1
    if m != 0:
        j = 2
    pn1 = j * (2.0*n+1.0)
    pn2 = float(mt.factorial(n-m))
    pn3 = float(mt.factorial(n+m))
    pn4 = pn2/pn3
    return (np.sqrt(pn1 * pn4)) * p

def C_or_J(queryC):
    Cnm = float(ggm02s[queryC].value)

    J_20 = 108263 * (10 ** -8)
    J_40 = -0.00000237091222
    J_60 =  0.00000000608347
    J_80 = -0.00000000001427

    C = queryC.split(' ')

    if C[1] == '2' and C[2] == '0': c_j = Cnm - J_20
    elif C[1] == '4' and C[2] == '0': c_j = Cnm - J_40
    elif C[1] == '6' and C[2] == '0': c_j = Cnm - J_60
    elif C[1] == '8' and C[2] == '0': c_j = Cnm - J_80
    else: c_j = Cnm


    return c_j



def get_N(data):
    cos = mt.cos
    sin = mt.sin
    sqrt = mt.sqrt

    a  = 6378137
    GM = 3968005 * (10 ** 8)
    gamE = 9.7803267715
    k = 0.001931851353
    e2 = 0.00669438002290

    top = 1 + k * (mt.sin(mt.radians(90) - data.Lat) ** 2)
    bottom = mt.sqrt(1 - e2 * (mt.sin(mt.radians(90) - data.Lat)**2))
    gam = gamE * (top / bottom)


    first = GM / (gam * data.r)

    outerSum = 0
    for n in range(2,20):
        innerSum = 0
        for m in range(0,n):
            queryC = 'C '+str(n)+' '+str(m)
            dCnm = C_or_J(queryC)
            if m == 0:
                continue
            queryS = 'S '+str(n)+' '+str(m)
            Snm = float(ggm02s[queryS].value)

            t = cos(mt.radians(90)-data.Lat)
            
            pnm = get_normilized_p(n,m,t)
            # pnm = sympy.assoc_legendre(n, m, t)
            innerSum += (dCnm * cos(m * data.Long) + Snm * sin(m * data.Long))*pnm

        outerSum += ((a/data.r)**n) * innerSum
    N = first * outerSum
    return N


if __name__ == '__main__':


    linesFile = RW.readFile('grvfld.ggm02s')
    ggm02s = RW.organizeLines(linesFile)


    TrignetStations= {'HNUS': TrigStations([34,25,28.6671],[19,13,23.0264],[4973168.840,1734085.512,-3585434.051]),
                      'PRET': TrigStations([25,43,55.2935],[28,16,57.4873],[5064032.237,2724721.031,-2752950.762]),
                      'RBAY': TrigStations([28,47,43.9616],[32,4,42.1896], [4739765.776,2970758.460,-3054077.535]),
                      'TDOU': TrigStations([23,4,47.6714], [30,23,2.4297], [5064840.815,2969624.535,-2485109.939]),
                      'ULDI': TrigStations([28,17,35.2196],[31,25,15.3309],[4796680.897,2930311.589,-3005435.714])}

    for name,data in TrignetStations.items():
        print (name, get_N(data))
