import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

h = 6.63e-34
c = 3e8

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

DirectAllowed = (alpha*hv)**2
IndirectAllowed = (alpha*hv)**0.5
DirectDisallowed = (alpha*hv)**(2/3)
IndirectDisallowed = (alpha*hv)**(1/3)

slope, intercept, r_value, p_value, std_err = stats.linregress(hv[425:452],DirectAllowed[425:452])
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(hv[480:490],DirectAllowed[480:490])
y = slope * xgen + intercept
y2 = slope2 * xgen + intercept2

slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(hv[425:452],IndirectAllowed[425:452])
slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(hv[480:490],IndirectAllowed[480:490])

y3 = slope3 * xgen + intercept3
y4 = slope4 * xgen + intercept4

slope5, intercept5, r_value5, p_value5, std_err5 = stats.linregress(hv[425:452],DirectDisallowed[425:452])
slope6, intercept6, r_value6, p_value6, std_err6 = stats.linregress(hv[480:490],DirectDisallowed[480:490])

y5 = slope5 * xgen + intercept5
y6 = slope6 * xgen + intercept6

slope7, intercept7, r_value7, p_value7, std_err7 = stats.linregress(hv[425:452],IndirectDisallowed[425:452])
slope8, intercept8, r_value8, p_value8, std_err8 = stats.linregress(hv[480:490],IndirectDisallowed[480:490])

y7 = slope7 * xgen + intercept7
y8 = slope8 * xgen + intercept8

line1start = (min(xgen),min(y))
line1end = (max(xgen),max(y))

line2start = (min(xgen),min(y2))
line2end = (max(xgen),max(y2))

line3start = (min(xgen),min(y3))
line3end = (max(xgen),max(y3))

line4start = (min(xgen),min(y4))
line4end = (max(xgen),max(y4))

line5start = (min(xgen),min(y5))
line5end = (max(xgen),max(y5))

line6start = (min(xgen),min(y6))
line6end = (max(xgen),max(y6))

line7start = (min(xgen),min(y7))
line7end = (max(xgen),max(y7))

line8start = (min(xgen),min(y8))
line8end = (max(xgen),max(y8))


DirectAllowedIntercept = line_intersection((line1start,line1end),(line2start,line2end))
IndirectAllowedIntercept = line_intersection((line3start,line3end),(line4start,line4end))
DirectDisallowedIntercept = line_intersection((line5start,line5end),(line6start,line6end))
IndirectDisallowedIntercept = line_intersection((line7start,line7end),(line8start,line8end))

DirAllow = np.around(DirectAllowedIntercept[0],3)
IndAllow = np.around(IndirectAllowedIntercept[0],3)
DirDisallow = np.around(DirectDisallowedIntercept[0],3)
IndDisallow = np.around(IndirectDisallowedIntercept[0],3)


plt.figure(11)
plt.semilogy(hv,alpha)
plt.xlabel('hv (eV)')
plt.ylabel('log α (cm^-1)')
plt.title('Absorption coefficent')
plt.plot()

plt.figure(2)
plt.plot(hv,DirectAllowed)
plt.xlabel('hv (eV)')
plt.ylabel('αhv^2 (cm^-1 eV)^2')
plt.title(f'Direct Bandgap (Allowed), Bandgap = {DirAllow}eV')

plt.plot(xgen,y,linestyle='dashed')
plt.plot(xgen,y2,linestyle='dashed')

plt.ylim(min(DirectAllowed),max(DirectAllowed))

plt.show()

plt.figure(3)
plt.plot(hv,IndirectAllowed)
plt.xlabel('hv (eV)')
plt.ylabel('αhv^1/2 (cm^-1 eV)^1/2')
plt.title(f'Indirect Bandgap (Allowed), Bandgap = {IndAllow}eV')

plt.plot(xgen,y3,linestyle='dashed')
plt.plot(xgen,y4,linestyle='dashed')

plt.ylim(min(IndirectAllowed),max(IndirectAllowed))

plt.show()

plt.figure(4)
plt.plot(hv,DirectDisallowed)
plt.xlabel('hv (eV)')
plt.ylabel('αhv^2/3 (cm^-1 eV)^2/3')
plt.title(f'Direct Bandgap (Disllowed), Bandgap = {DirDisallow}eV')

plt.plot(xgen,y5,linestyle='dashed')
plt.plot(xgen,y6,linestyle='dashed')

plt.ylim(min(DirectDisallowed),max(DirectDisallowed))

plt.show()

plt.figure(5)
plt.plot(hv,IndirectDisallowed)
plt.xlabel('hv (eV)')
plt.ylabel('αhv^1/3 (cm^-1 eV)^1/3')
plt.title(f'Indirect Bandgap (Disallowed), Bandgap = {IndDisallow}eV')

plt.plot(xgen,y7,linestyle='dashed')
plt.plot(xgen,y8,linestyle='dashed')

plt.ylim(min(IndirectDisallowed),max(IndirectDisallowed))

plt.show()

thicc = np.arange(0,500.01e-7,0.01e-7)

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



plt.figure(10)
RelativeIntensity = np.exp((-max(alpha) * thicc))
plt.plot((thicc*1e7),RelativeIntensity*100)
plt.xlabel('Sample thickness (nm)')
plt.ylabel('Relative Intesnity (%)')
plt.title('Transmission of light through hBN sample: ' + str(np.around(RelativeIntensity[25000] * 100,2))+'% at 250nm')

plt.figure(6)
plt.plot(Array20x,Array20y)
plt.title('20k PL Sample')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()

plt.figure(7)
plt.plot(Array290x,Array290y)
plt.title('290k PL Sample')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()

plt.figure(8)
plt.plot(SubArray290x,SubArray290y)
plt.title('290k PL Substrate')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()

plt.figure(9)
plt.plot(SubArray8x,SubArray8y)
plt.title('8k PL Substrate')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()

for i in range(0,len(SubArray8y)):
    if SubArray8y[i] > 150:
        SubArray8y[i] = np.mean(SubArray8y)
        
plt.figure(10)
plt.plot(SubArray8x,SubArray8y)
plt.title('8k Substrate PL Sample')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()    


NormArray290y = Array290y / max(Array290y)
NormArray20y = Array20y / max(Array20y)

NormSubArray290y = SubArray290y / max(SubArray290y)
NormSubArray8y = SubArray8y / max(SubArray8y)


for i in range(0,len(NormSubArray290y)):
    if ((NormSubArray290y[i] - NormSubArray290y[i-1]) / (NormSubArray290y[i] - NormSubArray290y[i-1])) > 250:
       NormSubArray290y[i] = NormSubArray290y[i-1]
    elif ((NormSubArray290y[i] - NormSubArray290y[i-1]) / (NormSubArray290y[i] - NormSubArray290y[i-1])) < -250:
        NormSubArray290y[i] = NormSubArray290y[i-1]
    else:
        pass


    
Diff1 = NormArray290y - NormSubArray290y
Diff2 = NormArray20y - NormSubArray8y

for i in range(len(Diff1)):
    if Diff1[i] < 0:
        Diff1[i] = 0
    else:
        pass
    
    if Diff2[i] < 0:
        Diff2[i] = 0
    else:
        pass

        

plt.figure(11)
plt.plot(SubArray290x,Diff1)
plt.title('290K Sample with Substrate mitigated')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()  

plt.figure(12)
plt.plot(SubArray8x,Diff2)
plt.title('20/8K Sample with Substrate mitigated')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (arb)')
plt.show()  