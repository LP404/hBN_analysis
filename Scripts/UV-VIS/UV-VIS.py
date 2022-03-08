import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

h = 6.63e-34
c = 3e8

def merge(a, b):
    n_a = len(a)
    n = min(n_a, len(b))
    m = 0
    for i in range(1, n + 1):
        if b[n - i] == a[n_a - 1 - m]:
            m += 1
        else:
            m = 0
    return a + b[m:]

def shiftFunc(Array,Shift):
    # A quick check to see if the desired shift length exceeds the length of the array
    if Shift > len(Array):
        print('Array Shift exceeds length of array. Function will return input Array')
        return Array
    else:
        #Seperates the Array into two parts at the point where it is to be shifted the second part is then moved to be in front and the arrays are concatenated together to make a shifted array
        ArrayFront, ArrayBack = Array[0:int(Shift)],Array[int(Shift):len(Array)]
        ShiftedArray = np.concatenate([ArrayBack,ArrayFront])
    return ShiftedArray

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


#Arrays are flipped so when wavelengths are converted to eV they are in ascending order
SampleReflect = np.flip(np.loadtxt('hBN106_Reflect.txt',delimiter=',',skiprows = 2).T)
SampleTransmit = np.flip(np.loadtxt('hBN106_Slow.txt',delimiter=',',skiprows = 2).T)
SubstrateReflect = np.flip(np.loadtxt('Substrate_Reflect.txt',delimiter=',',skiprows = 2).T)
SubstrateTransmit = np.flip(np.loadtxt('Substrate_Slow.txt',delimiter=',',skiprows = 2).T)

Lambda_300nm_20 = np.loadtxt('hBN106_PL/20K_session_2022_02_10/hBN106_300nm.txt').T
Lambda_400nm_20 = np.loadtxt('hBN106_PL/20K_session_2022_02_10/hBN106_400nm.txt').T
Lambda_500nm_20 = np.loadtxt('hBN106_PL/20K_session_2022_02_10/hBN106_500nm.txt').T
Lambda_600nm_20 = np.loadtxt('hBN106_PL/20K_session_2022_02_10/hBN106_600nm.txt').T
Lambda_700nm_20 = np.loadtxt('hBN106_PL/20K_session_2022_02_10/hBN106_700nm.txt').T
Lambda_800nm_20 = np.loadtxt('hBN106_PL/20K_session_2022_02_10/hBN106_800nm.txt').T
Lambda_900nm_20 = np.loadtxt('hBN106_PL/20K_session_2022_02_10/hBN106_900nm.txt').T

Lambda_300nm_290 = np.loadtxt('hBN106_PL/290K_session_2022_02_10/hBN106_300nm.txt').T
Lambda_400nm_290 = np.loadtxt('hBN106_PL/290K_session_2022_02_10/hBN106_400nm.txt').T
Lambda_500nm_290 = np.loadtxt('hBN106_PL/290K_session_2022_02_10/hBN106_500nm.txt').T
Lambda_600nm_290 = np.loadtxt('hBN106_PL/290K_session_2022_02_10/hBN106_600nm.txt').T
Lambda_700nm_290 = np.loadtxt('hBN106_PL/290K_session_2022_02_10/hBN106_700nm.txt').T
Lambda_800nm_290 = np.loadtxt('hBN106_PL/290K_session_2022_02_10/hBN106_800nm.txt').T
Lambda_900nm_290 = np.loadtxt('hBN106_PL/290K_session_2022_02_10/hBN106_900nm.txt').T

Substrate_300nm_290 = np.loadtxt('Substrate_PL/Sapphire290K_300.txt').T
Substrate_400nm_290 = np.loadtxt('Substrate_PL/Sapphire290K_400.txt').T
Substrate_500nm_290 = np.loadtxt('Substrate_PL/Sapphire290K_500.txt').T
Substrate_600nm_290 = np.loadtxt('Substrate_PL/Sapphire290K_600.txt').T
Substrate_700nm_290 = np.loadtxt('Substrate_PL/Sapphire290K_700.txt').T
Substrate_800nm_290 = np.loadtxt('Substrate_PL/Sapphire290K_800.txt').T
Substrate_900nm_290 = np.loadtxt('Substrate_PL/Sapphire290K_900.txt').T

Substrate_300nm_8 = np.loadtxt('Substrate_PL/Sapphire8K_300.txt').T
Substrate_400nm_8 = np.loadtxt('Substrate_PL/Sapphire8K_400.txt').T
Substrate_500nm_8 = np.loadtxt('Substrate_PL/Sapphire8K_500.txt').T
Substrate_600nm_8 = np.loadtxt('Substrate_PL/Sapphire8K_600.txt').T
Substrate_700nm_8 = np.loadtxt('Substrate_PL/Sapphire8K_700.txt').T
Substrate_800nm_8 = np.loadtxt('Substrate_PL/Sapphire8K_800.txt').T
Substrate_900nm_8 = np.loadtxt('Substrate_PL/Sapphire8K_900.txt').T

hv = ((h * c) / (SubstrateTransmit[1] * 1e-9)) * 6.242e18

T_film = SampleTransmit[0]  / SubstrateTransmit[0]
R_film = SampleReflect[0] / SubstrateReflect[0]

#T_film = SubstrateTransmit[0]
#R_film = SubstrateReflect[0]

xgen = np.arange(2,6.1,0.1)
alpha = (np.log((1/T_film))) / 2.5e-5
#alpha = np.log( ( ((1- R_film)**2) / T_film) ) / 2.5e-5 
#alpha = np.log(( ((1- R_film)**2) / (2 * T_film)) + np.sqrt( (( ((1- R_film)**4) / (4 * T_film**2)) + (R_film**2)) )) / 2.5e-5

# DirectAllowed = (alpha*hv)**2
# IndirectAllowed = (alpha*hv)**0.5
# DirectDisallowed = (alpha*hv)**(2/3)
# IndirectDisallowed = (alpha*hv)**(1/3)

# slope, intercept, r_value, p_value, std_err = stats.linregress(hv[375:457],DirectAllowed[375:457])
# slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(hv[480:490],DirectAllowed[480:490])
# y = slope * xgen + intercept
# y2 = slope2 * xgen + intercept2

# slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(hv[341:439],IndirectAllowed[341:439])
# slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(hv[480:490],IndirectAllowed[480:490])

# y3 = slope3 * xgen + intercept3
# y4 = slope4 * xgen + intercept4

# slope5, intercept5, r_value5, p_value5, std_err5 = stats.linregress(hv[379:457],DirectDisallowed[379:457])
# slope6, intercept6, r_value6, p_value6, std_err6 = stats.linregress(hv[480:490],DirectDisallowed[480:490])

# y5 = slope5 * xgen + intercept5
# y6 = slope6 * xgen + intercept6

# slope7, intercept7, r_value7, p_value7, std_err7 = stats.linregress(hv[383:461],IndirectDisallowed[383:461])
# slope8, intercept8, r_value8, p_value8, std_err8 = stats.linregress(hv[480:490],IndirectDisallowed[480:490])

# y7 = slope7 * xgen + intercept7
# y8 = slope8 * xgen + intercept8

# line1start = (min(xgen),min(y))
# line1end = (max(xgen),max(y))

# line2start = (min(xgen),min(y2))
# line2end = (max(xgen),max(y2))

# line3start = (min(xgen),min(y3))
# line3end = (max(xgen),max(y3))

# line4start = (min(xgen),min(y4))
# line4end = (max(xgen),max(y4))

# line5start = (min(xgen),min(y5))
# line5end = (max(xgen),max(y5))

# line6start = (min(xgen),min(y6))
# line6end = (max(xgen),max(y6))

# line7start = (min(xgen),min(y7))
# line7end = (max(xgen),max(y7))

# line8start = (min(xgen),min(y8))
# line8end = (max(xgen),max(y8))


# DirectAllowedIntercept = line_intersection((line1start,line1end),(line2start,line2end))
# IndirectAllowedIntercept = line_intersection((line3start,line3end),(line4start,line4end))
# DirectDisallowedIntercept = line_intersection((line5start,line5end),(line6start,line6end))
# IndirectDisallowedIntercept = line_intersection((line7start,line7end),(line8start,line8end))

# DirAllow = np.around(DirectAllowedIntercept[0],3)
# IndAllow = np.around(IndirectAllowedIntercept[0],3)
# DirDisallow = np.around(DirectDisallowedIntercept[0],3)
# IndDisallow = np.around(IndirectDisallowedIntercept[0],3)


# plt.figure(11)
# plt.semilogy(hv,alpha)
# plt.xlabel('hv (eV)')
# plt.ylabel('log α (cm^-1)')
# plt.title('Absorbtion coefficent')
# plt.plot()

# plt.figure(2)
# plt.plot(hv,DirectAllowed)
# plt.xlabel('hv (eV)')
# plt.ylabel('αhv^2 (cm^-1 eV)^2')
# plt.title(f'Direct Bandgap (Allowed), Bandgap = {DirAllow}eV')

# plt.plot(xgen,y,linestyle='dashed')
# plt.plot(xgen,y2,linestyle='dashed')

# plt.ylim(min(DirectAllowed),max(DirectAllowed))

# plt.show()

# plt.figure(3)
# plt.plot(hv,IndirectAllowed)
# plt.xlabel('hv (eV)')
# plt.ylabel('αhv^1/2 (cm^-1 eV)^1/2')
# plt.title(f'Indirect Bandgap (Allowed), Bandgap = {IndAllow}eV')

# plt.plot(xgen,y3,linestyle='dashed')
# plt.plot(xgen,y4,linestyle='dashed')

# plt.ylim(min(IndirectAllowed),max(IndirectAllowed))

# plt.show()

# plt.figure(4)
# plt.plot(hv,DirectDisallowed)
# plt.xlabel('hv (eV)')
# plt.ylabel('αhv^2/3 (cm^-1 eV)^2/3')
# plt.title(f'Direct Bandgap (Disllowed), Bandgap = {DirDisallow}eV')

# plt.plot(xgen,y5,linestyle='dashed')
# plt.plot(xgen,y6,linestyle='dashed')

# plt.ylim(min(DirectDisallowed),max(DirectDisallowed))

# plt.show()

# plt.figure(5)
# plt.plot(hv,IndirectDisallowed)
# plt.xlabel('hv (eV)')
# plt.ylabel('αhv^1/3 (cm^-1 eV)^1/3')
# plt.title(f'Indirect Bandgap (Disallowed), Bandgap = {IndDisallow}eV')

# plt.plot(xgen,y7,linestyle='dashed')
# plt.plot(xgen,y8,linestyle='dashed')

# plt.ylim(min(IndirectDisallowed),max(IndirectDisallowed))

plt.show()

thicc = np.arange(0,500.01e-7,0.01e-7)

plt.figure(10)
RelativeIntensity = np.exp((-max(alpha) * thicc))
plt.plot((thicc*1e7),RelativeIntensity*100)
plt.xlabel('Sample thickness (nm)')
plt.ylabel('Relative Intesnity (%)')
plt.title('Absorbtion of light through hBN sample')

plt.figure(6)
plt.plot(Lambda_300nm_20[0],Lambda_300nm_20[1], color = 'blue')
plt.plot(Lambda_400nm_20[0],Lambda_400nm_20[1], color = 'blue')
plt.plot(Lambda_500nm_20[0],Lambda_500nm_20[1], color = 'blue')
plt.plot(Lambda_600nm_20[0],Lambda_600nm_20[1], color = 'blue')
plt.plot(Lambda_700nm_20[0],Lambda_700nm_20[1], color = 'blue')
plt.plot(Lambda_800nm_20[0],Lambda_800nm_20[1], color = 'blue')
plt.plot(Lambda_900nm_20[0],Lambda_900nm_20[1], color = 'blue')
plt.title('20k PL Sample')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()

plt.figure(7)
plt.plot(Lambda_300nm_290[0],Lambda_300nm_290[1], color = 'blue')
plt.plot(Lambda_400nm_290[0],Lambda_400nm_290[1], color = 'blue')
plt.plot(Lambda_500nm_290[0],Lambda_500nm_290[1], color = 'blue')
plt.plot(Lambda_600nm_290[0],Lambda_600nm_290[1], color = 'blue')
plt.plot(Lambda_700nm_290[0],Lambda_700nm_290[1], color = 'blue')
plt.plot(Lambda_800nm_290[0],Lambda_800nm_290[1], color = 'blue')
plt.plot(Lambda_900nm_290[0],Lambda_900nm_290[1], color = 'blue')
plt.title('290k PL Sample')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()

plt.figure(8)
plt.plot(Substrate_300nm_290[0],Substrate_300nm_290[1], color = 'blue')
plt.plot(Substrate_400nm_290[0],Substrate_400nm_290[1], color = 'blue')
plt.plot(Substrate_500nm_290[0],Substrate_500nm_290[1], color = 'blue')
plt.plot(Substrate_600nm_290[0],Substrate_600nm_290[1], color = 'blue')
plt.plot(Substrate_700nm_290[0],Substrate_700nm_290[1], color = 'blue')
plt.plot(Substrate_800nm_290[0],Substrate_800nm_290[1], color = 'blue')
plt.plot(Substrate_900nm_290[0],Substrate_900nm_290[1], color = 'blue')
plt.title('290k PL Substrate')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()

plt.figure(9)
plt.plot(Substrate_300nm_8[0],Substrate_300nm_8[1], color = 'blue')
plt.plot(Substrate_400nm_8[0],Substrate_400nm_8[1], color = 'blue')
plt.plot(Substrate_500nm_8[0],Substrate_500nm_8[1], color = 'blue')
plt.plot(Substrate_600nm_8[0],Substrate_600nm_8[1], color = 'blue')
plt.plot(Substrate_700nm_8[0],Substrate_700nm_8[1], color = 'blue')
plt.plot(Substrate_800nm_8[0],Substrate_800nm_8[1], color = 'blue')
plt.plot(Substrate_900nm_8[0],Substrate_900nm_8[1], color = 'blue')
plt.title('8k PL Substrate')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()


Array20x = np.concatenate([Lambda_300nm_20[0],Lambda_400nm_20[0],Lambda_500nm_20[0],Lambda_600nm_20[0],Lambda_700nm_20[0],Lambda_800nm_20[0],Lambda_900nm_20[0]],axis=0)
Array20y = np.concatenate([Lambda_300nm_20[1],Lambda_400nm_20[1],Lambda_500nm_20[1],Lambda_600nm_20[1],Lambda_700nm_20[1],Lambda_800nm_20[1],Lambda_900nm_20[1]],axis=0)

Array290x = np.concatenate([Lambda_300nm_20[0],Lambda_400nm_290[0],Lambda_500nm_290[0],Lambda_600nm_290[0],Lambda_700nm_290[0],Lambda_800nm_290[0],Lambda_900nm_290[0]],axis=0)
Array290y = np.concatenate([Lambda_300nm_290[1],Lambda_400nm_290[1],Lambda_500nm_290[1],Lambda_600nm_290[1],Lambda_700nm_290[1],Lambda_800nm_290[1],Lambda_900nm_290[1]],axis=0)

SubArray290x = np.concatenate([Substrate_300nm_290[0],Substrate_400nm_290[0],Substrate_500nm_290[0],Substrate_600nm_290[0],Substrate_700nm_290[0],Substrate_800nm_290[0],Substrate_900nm_290[0]],axis=0)
SubArray290y = np.concatenate([Substrate_300nm_290[1],Substrate_400nm_290[1],Substrate_500nm_290[1],Substrate_600nm_290[1],Substrate_700nm_290[1],Substrate_800nm_290[1],Substrate_900nm_290[1]],axis=0)

SubArray8x = np.concatenate([Substrate_300nm_8[0],Substrate_400nm_8[0],Substrate_500nm_8[0],Substrate_600nm_8[0],Substrate_700nm_8[0],Substrate_800nm_8[0],Substrate_900nm_8[0]],axis=0)
SubArray8y = np.concatenate([Substrate_300nm_8[1],Substrate_400nm_8[1],Substrate_500nm_8[1],Substrate_600nm_8[1],Substrate_700nm_8[1],Substrate_800nm_8[1],Substrate_900nm_8[1]],axis=0)

Inds1 = Array20x.argsort()
Array20x = Array20x[Inds1[::1]]
Array20y = Array20y[Inds1[::1]]

Inds2 = Array290x.argsort()
Array290x = Array290x[Inds2[::1]]
Array290y = Array290y[Inds2[::1]]

Inds3 = SubArray290x.argsort()
SubArray290x = SubArray290x[Inds3[::1]]
SubArray290y = SubArray290y[Inds3[::1]]

Inds4 = SubArray8x.argsort()
SubArray8x = SubArray8x[Inds4[::1]]
SubArray8y = SubArray8y[Inds4[::1]]







# ArrayFront300_290, ArrayBack300_290 = Lambda_300nm_290[1][0:int(len(Lambda_300nm_290[1])/2)],Lambda_300nm_290[1][int(len(Lambda_300nm_290[0])/2):len(Lambda_300nm_290[1])]
# ArrayFront400_290, ArrayBack400_290 = Lambda_400nm_290[1][0:int(len(Lambda_400nm_290[1])/2)],Lambda_400nm_290[1][int(len(Lambda_400nm_290[0])/2):len(Lambda_400nm_290[1])]
# ArrayFront500_290, ArrayBack500_290 = Lambda_500nm_290[1][0:int(len(Lambda_500nm_290[1])/2)],Lambda_500nm_290[1][int(len(Lambda_500nm_290[0])/2):len(Lambda_500nm_290[1])]
# ArrayFront600_290, ArrayBack600_290 = Lambda_600nm_290[1][0:int(len(Lambda_600nm_290[1])/2)],Lambda_600nm_290[1][int(len(Lambda_600nm_290[0])/2):len(Lambda_600nm_290[1])]
# ArrayFront700_290, ArrayBack700_290 = Lambda_700nm_290[1][0:int(len(Lambda_700nm_290[1])/2)],Lambda_700nm_290[1][int(len(Lambda_700nm_290[0])/2):len(Lambda_700nm_290[1])]
# ArrayFront800_290, ArrayBack800_290 = Lambda_800nm_290[1][0:int(len(Lambda_800nm_290[1])/2)],Lambda_800nm_290[1][int(len(Lambda_800nm_290[0])/2):len(Lambda_800nm_290[1])]
# ArrayFront900_290, ArrayBack900_290 = Lambda_900nm_290[1][0:int(len(Lambda_900nm_290[1])/2)],Lambda_900nm_290[1][int(len(Lambda_900nm_290[0])/2):len(Lambda_900nm_290[1])]

# ArrayFront300_20, ArrayBack300_20 = Lambda_300nm_20[1][0:int(len(Lambda_300nm_20[1])/2)],Lambda_300nm_20[1][int(len(Lambda_300nm_20[0])/2):len(Lambda_300nm_20[1])]
# ArrayFront400_20, ArrayBack400_20 = Lambda_400nm_20[1][0:int(len(Lambda_400nm_20[1])/2)],Lambda_400nm_20[1][int(len(Lambda_400nm_20[0])/2):len(Lambda_400nm_20[1])]
# ArrayFront500_20, ArrayBack500_20 = Lambda_500nm_20[1][0:int(len(Lambda_500nm_20[1])/2)],Lambda_500nm_20[1][int(len(Lambda_500nm_20[0])/2):len(Lambda_500nm_20[1])]
# ArrayFront600_20, ArrayBack600_20 = Lambda_600nm_20[1][0:int(len(Lambda_600nm_20[1])/2)],Lambda_600nm_20[1][int(len(Lambda_600nm_20[0])/2):len(Lambda_600nm_20[1])]
# ArrayFront700_20, ArrayBack700_20 = Lambda_700nm_20[1][0:int(len(Lambda_700nm_20[1])/2)],Lambda_700nm_20[1][int(len(Lambda_700nm_20[0])/2):len(Lambda_700nm_20[1])]
# ArrayFront800_20, ArrayBack800_20 = Lambda_800nm_20[1][0:int(len(Lambda_800nm_20[1])/2)],Lambda_800nm_20[1][int(len(Lambda_800nm_20[0])/2):len(Lambda_800nm_20[1])]
# ArrayFront900_20, ArrayBack900_20 = Lambda_900nm_20[1][0:int(len(Lambda_900nm_20[1])/2)],Lambda_900nm_20[1][int(len(Lambda_900nm_20[0])/2):len(Lambda_900nm_20[1])]

# SubArrayFront300_290, SubArrayBack300_290 =Substrate_300nm_290[1][0:int(len(Substrate_300nm_290[1])/2)],Substrate_300nm_290[1][int(len(Substrate_300nm_290[0])/2):len(Substrate_300nm_290[1])]
# SubArrayFront400_290, SubArrayBack400_290 =Substrate_400nm_290[1][0:int(len(Substrate_400nm_290[1])/2)],Substrate_400nm_290[1][int(len(Substrate_400nm_290[0])/2):len(Substrate_400nm_290[1])]
# SubArrayFront500_290, SubArrayBack500_290 =Substrate_500nm_290[1][0:int(len(Substrate_500nm_290[1])/2)],Substrate_500nm_290[1][int(len(Substrate_500nm_290[0])/2):len(Substrate_500nm_290[1])]
# SubArrayFront600_290, SubArrayBack600_290 =Substrate_600nm_290[1][0:int(len(Substrate_600nm_290[1])/2)],Substrate_600nm_290[1][int(len(Substrate_600nm_290[0])/2):len(Substrate_600nm_290[1])]
# SubArrayFront700_290, SubArrayBack700_290 =Substrate_700nm_290[1][0:int(len(Substrate_700nm_290[1])/2)],Substrate_700nm_290[1][int(len(Substrate_700nm_290[0])/2):len(Substrate_700nm_290[1])]
# SubArrayFront800_290, SubArrayBack800_290 =Substrate_800nm_290[1][0:int(len(Substrate_800nm_290[1])/2)],Substrate_800nm_290[1][int(len(Substrate_800nm_290[0])/2):len(Substrate_800nm_290[1])]
# SubArrayFront900_290, SubArrayBack900_290 =Substrate_900nm_290[1][0:int(len(Substrate_900nm_290[1])/2)],Substrate_900nm_290[1][int(len(Substrate_900nm_290[0])/2):len(Substrate_900nm_290[1])]

# SubArrayFront300_8, SubArrayBack300_8 =Substrate_300nm_8[1][0:int(len(Substrate_300nm_8[1])/2)],Substrate_300nm_8[1][int(len(Substrate_300nm_8[0])/2):len(Substrate_300nm_8[1])]
# SubArrayFront400_8, SubArrayBack400_8 =Substrate_400nm_8[1][0:int(len(Substrate_400nm_8[1])/2)],Substrate_400nm_8[1][int(len(Substrate_400nm_8[0])/2):len(Substrate_400nm_8[1])]
# SubArrayFront500_8, SubArrayBack500_8 =Substrate_500nm_8[1][0:int(len(Substrate_500nm_8[1])/2)],Substrate_500nm_8[1][int(len(Substrate_500nm_8[0])/2):len(Substrate_500nm_8[1])]
# SubArrayFront600_8, SubArrayBack600_8 =Substrate_600nm_8[1][0:int(len(Substrate_600nm_8[1])/2)],Substrate_600nm_8[1][int(len(Substrate_600nm_8[0])/2):len(Substrate_600nm_8[1])]
# SubArrayFront700_8, SubArrayBack700_8 =Substrate_700nm_8[1][0:int(len(Substrate_700nm_8[1])/2)],Substrate_700nm_8[1][int(len(Substrate_700nm_8[0])/2):len(Substrate_700nm_8[1])]
# SubArrayFront800_8, SubArrayBack800_8 =Substrate_800nm_8[1][0:int(len(Substrate_800nm_8[1])/2)],Substrate_800nm_8[1][int(len(Substrate_800nm_8[0])/2):len(Substrate_800nm_8[1])]
# SubArrayFront900_8, SubArrayBack900_8 =Substrate_900nm_8[1][0:int(len(Substrate_900nm_8[1])/2)],Substrate_900nm_8[1][int(len(Substrate_900nm_8[0])/2):len(Substrate_900nm_8[1])]

# Arr290Avg1 = (ArrayBack300_290 + ArrayFront400_290) / 2
# Arr290Avg2 = (ArrayBack400_290 + ArrayFront500_290) / 2
# Arr290Avg3 = (ArrayBack500_290 + ArrayFront600_290) / 2
# Arr290Avg4 = (ArrayBack600_290 + ArrayFront700_290) / 2
# Arr290Avg5 = (ArrayBack700_290 + ArrayFront800_290) / 2
# Arr290Avg6 = (ArrayBack800_290 + ArrayFront900_290) / 2

# Arr20Avg1 = (ArrayBack300_20 + ArrayFront400_20) / 2
# Arr20Avg2 = (ArrayBack400_20 + ArrayFront500_20) / 2
# Arr20Avg3 = (ArrayBack500_20 + ArrayFront600_20) / 2
# Arr20Avg4 = (ArrayBack600_20 + ArrayFront700_20) / 2
# Arr20Avg5 = (ArrayBack700_20 + ArrayFront800_20) / 2
# Arr20Avg6 = (ArrayBack800_20 + ArrayFront900_20) / 2

# SubArr290Avg1 = (SubArrayBack300_290 + SubArrayFront400_290) / 2
# SubArr290Avg2 = (SubArrayBack400_290 + SubArrayFront500_290) / 2
# SubArr290Avg3 = (SubArrayBack500_290 + SubArrayFront600_290) / 2
# SubArr290Avg4 = (SubArrayBack600_290 + SubArrayFront700_290) / 2
# SubArr290Avg5 = (SubArrayBack700_290 + SubArrayFront800_290) / 2
# SubArr290Avg6 = (SubArrayBack800_290 + SubArrayFront900_290) / 2

# SubArr8Avg1 = (SubArrayBack300_8 + SubArrayFront400_8) / 2
# SubArr8Avg2 = (SubArrayBack400_8 + SubArrayFront500_8) / 2
# SubArr8Avg3 = (SubArrayBack500_8 + SubArrayFront600_8) / 2
# SubArr8Avg4 = (SubArrayBack600_8 + SubArrayFront700_8) / 2
# SubArr8Avg5 = (SubArrayBack700_8 + SubArrayFront800_8) / 2
# SubArr8Avg6 = (SubArrayBack800_8 + SubArrayFront900_8) / 2

# Array290 = np.concatenate([ArrayFront300_290,Arr20Avg1,Arr290Avg2,Arr290Avg3,Arr290Avg4,Arr290Avg5,Arr290Avg6,ArrayBack900_290], axis=0)
# Array20 = np.concatenate([ArrayFront300_20,Arr20Avg1,Arr20Avg2,Arr20Avg3,Arr20Avg4,Arr20Avg5,Arr20Avg6,ArrayBack900_290], axis=0)
# SubArray290 = np.concatenate([SubArrayFront300_290,SubArr290Avg1,SubArr290Avg2,SubArr290Avg3,SubArr290Avg4,SubArr290Avg5,SubArr290Avg6,SubArrayBack900_290], axis=0)
# SubArray8 = np.concatenate([SubArrayFront300_8,SubArr8Avg1,SubArr8Avg2,SubArr8Avg3,SubArr8Avg4,SubArr8Avg5,SubArr8Avg6,SubArrayBack900_8], axis=0)

# Array2901 = np.concatenate([ArrayFront300_290,ArrayBack400_290,Arr290Avg2,Arr290Avg3,Arr290Avg4,Arr290Avg5,Arr290Avg6,ArrayBack900_290],axis=0)

# Sample290_x = np.linspace(min(Lambda_300nm_290[0]),max(Lambda_900nm_290[0]),len(Array290))
# Sample20_x = np.linspace(min(Lambda_300nm_20[0]),max(Lambda_900nm_20[0]),len(Array20))
# Substrate290_x = np.linspace(min(Substrate_300nm_290[0]),max(Substrate_900nm_290[0]),len(SubArray290))
# Substrate8_x = np.linspace(min(Substrate_300nm_8[0]),max(Substrate_900nm_8[0]),len(SubArray8))