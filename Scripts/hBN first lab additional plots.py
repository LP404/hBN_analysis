import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

WDX_Energy = np.array([5,7,10,15])

L2B = np.array([44.36,69.70,72.16,31.43])
L2C = np.array([50.04,69.47,72.44,33.81])
L2N = np.array([85.93,104.86,106.58,55.05])

L1N = np.array([12.91,19.22,23.23,12.45])
L1O = np.array([0,23.43,24.27,274.72])

PET_Al = np.array([0,2,3.87,547.00])

EDX_Energy = np.array([10,15])
EDX_CutOff = np.array([7.47,13.21])

Ray_AbsorbAl = np.array([0,0,0.01,56.26,220.75,432.55,673.06,927.74,1199.55,1491.61,1787.58,2090.16,2394.36,2711.28,3030.95,3368.29,3693.88,4033.73,4396.11,4740.12])
Ray_DetectAl = np.array([0,0,0.01,54.21,210.16,405.74,620.56,838.62,1060.82,1287.84,1504.70,1710.59,1904.53,2091.31,2260.35,2430.87,2575.75,2709.04,2847.08,2948.85])
Ray_AbsorbB = np.array([6.44,20.03,31.63,28.05,23.11,19.63,17.04,15.26,13.70,12.39,11.39,10.47,9.85,9.45,8.64,8.27,8.00,7.51,7.20,6.98])
Ray_DetectB = np.array([6.30,18.55,27.51,24.11,19.89,16.95,14.74,13.23,11.88,10.75,9.90,9.09,8.56,8.22,7.51,7.19,6.95,6.53,6.26,6.07])
Ray_AbsorbN = np.array([20.91,104.11,196.81,195.00,168.96,148.12,131.49,119.74,109.13,99.65,92.50,85.83,81.24,78.35,72.20,69.38,67.29,65.53,61.10,59.32])
Ray_DetectN = np.array([20.55,97.17,172.26,168.10,145.63,128.03,113.80,103.81,94.67,86.49,80.38,74.55,70.63,68.11,62.77,60.35,58.51,55.26,53.14,51.59])
Ray_AbsorbO = np.array([0,0,17.77,190.48,418.81,648.92,883.05,1112.55,1348.80,1595.67,1837.36,2079.35,2316.32,2561.41,2806.15,3062.00,3304.15,3556.07,3826.63,4076.96])
Ray_DetectO = np.array([0,0,10.82,111.61,232.91,339.19,430.29,501.33,558.66,604.32,653.13,650.93,658.97,659.23,647.98,641.46,626.76,607.64,593.82,569.75])

BeamEnergy = np.arange(1,21,1)


plt.figure(1)
plt.title('LDEL2 Intensites')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,L2B, label = 'B', marker = 'x')
plt.plot(WDX_Energy,L2N, label = 'N', marker = 'o')
plt.plot(WDX_Energy,L2C, label = 'C', marker = 's')
plt.legend()
plt.xticks(np.arange(5,16,1))

plt.figure(2)
plt.title('LDEL1 Intensites')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,L1N, label = 'N', marker = 'x')
plt.plot(WDX_Energy,L1O, label = 'O', marker = 'o')
plt.legend()
plt.xticks(np.arange(5,16,1))

plt.figure(3)
plt.title('PETJ Intensites')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.semilogy(WDX_Energy,PET_Al, label = 'Al', marker = 'x')
plt.legend()
plt.xticks(np.arange(5,16,1))


plt.figure(30)
plt.title('PETJ Intensites')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,PET_Al, label = 'Al', marker = 'x')
plt.legend()
plt.xticks(np.arange(5,16,1))

plt.figure(4)
plt.title('Nitrogen Intensites by crystal')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,L2N, label = 'LDEL2', marker = 'x')
plt.plot(WDX_Energy,L1N, label = 'LDEL1', marker = 'o')
plt.legend()
plt.xticks(np.arange(5,16,1))

xGen = np.linspace(0,20,10001)
m, c, r, p, std_err = stats.linregress(EDX_Energy,EDX_CutOff)
yGen = m * xGen + c

plt.figure(5)
plt.title('Cutoff Energy for EDX')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Cutoff Energy (keV)')
plt.scatter(EDX_Energy,EDX_CutOff, label = 'Experemental Data')
plt.plot(xGen,yGen, label = 'Line Fit \n m = '+str(np.around(m,3))+'\n c = '+str(np.around(c,3)), linestyle = ':')
plt.legend()

plt.figure(6)
plt.title('Detection of X-Rays 1')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,Ray_AbsorbAl, label = 'I_total (Al)', marker = 'x')
plt.plot(BeamEnergy,Ray_DetectAl, label = 'I_detected (Al)', marker = 'x')
plt.plot(BeamEnergy,Ray_AbsorbO, label = 'I_total (O)', marker = 'o')
plt.plot(BeamEnergy,Ray_DetectO, label = 'I_detected (O)', marker = 'o')
plt.legend()

plt.figure(7)
plt.title('Detection of X-Rays 2')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,Ray_AbsorbB, label = 'I_total (B)', marker = 'x')
plt.plot(BeamEnergy,Ray_DetectB, label = 'I_detected (B)', marker = 'x')
plt.plot(BeamEnergy,Ray_AbsorbN, label = 'I_total (N)', marker = 'o')
plt.plot(BeamEnergy,Ray_DetectN, label = 'I_detected (B)', marker = 'o')
plt.legend()

plt.figure(8)
plt.title('ΔIntensity of X-Rays 1')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('ΔIntensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_AbsorbB - Ray_DetectB), label = 'ΔI (B)', marker = 'x')
plt.plot(BeamEnergy,(Ray_AbsorbN - Ray_DetectN), label = 'ΔI (N)', marker = 'o')
plt.legend()

plt.figure(9)
plt.title('ΔIntensity of X-Rays 2')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('ΔIntensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_AbsorbAl - Ray_DetectAl), label = 'ΔI (Al)', marker = 'x')
plt.plot(BeamEnergy,(Ray_AbsorbO - Ray_DetectO), label = 'ΔI (O)', marker = 'o')
plt.legend()
