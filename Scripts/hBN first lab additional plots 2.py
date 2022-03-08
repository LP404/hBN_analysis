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
EDX_Energy2 = np.array([2,3,5,7,10,12,15])

EDX_CutOff = np.array([6.64,11.76])
EDX_CutOff1 = np.array([7.47,13.21])

# EDX_CutOff2_1 = [4.09,3.32,4.37,4.23,5.38,6.29,7.74]
# EDX_CutOff2_10 = [2.77,3.08,4.10,3.82,4.86,5.62,6.87]

EDX_CutOff2_1 = np.array([1.95,2.99,4.28,4.23,5.38,6.29,7.74])
EDX_CutOff2_10 = np.array([1.90,2.90,4.06,3.82,4.86,5.62,6.87])

DeltaEDX1 = EDX_Energy2 - EDX_CutOff2_1
DeltaEDX10 = EDX_Energy2 - EDX_CutOff2_10

Ray_AbsorbAl_200 = np.array([0,0,0,0.01,43.31,214.46,453.82,724.70,1004.51,1322.22,1628.55,1936.70,2249.50,2573.57,2895.99,3238.39,3570.42,3917.07,4261.61,4628.86])
Ray_DetectAl_200 = np.array([0,0,0,0.01,40.54,198.18,412.81,646.76,877.80,1128.30,1354.43,1567.11,1768.83,1963.08,2137.60,2311.64,2457.30,2601.30,2726.82,2844.39])
Ray_AbsorbB_200 = np.array([6.44,20.04,35.45,51.06,51.17,44.42,38.51,33.58,30.51,26.59,24.19,22.60,21.16,19.67,18.83,17.66,16.84,15.94,15.39,14.49])
Ray_DetectB_200 = np.array([6.30,18.55,30.31,39.56,38.11,32.91,28.63,25.07,22.88,19.97,18.23,17.08,16.01,14.89,14.27,13.40,12.80,12.12,11.71,11.02])
Ray_AbsorbN_200 = np.array([20.90,104.14,213.02,333.16,362.95,329.85,293.68,261.39,240.78,212.67,195.49,184.06,173.54,162.59,156.24,147.27,141.23,134.26,130.07,122.95])
Ray_DetectN_200 = np.array([20.54,97.16,184.19,261.54,272.19,245.39,218.88,195.41,180.72,159.87,147.44,139.22,131.34,123.18,118.43,111.75,107.38,102.11,98.88,93.52])
Ray_AbsorbO_200 = np.array([0,0,0,4.43,141.82,387.57,650.81,916.26,1167.23,1447.04,1702.00,1950.61,2197.50,2451.45,2698.38,2959.52,3208.34,3467.10,3721.43,3992.92])
Ray_DetectO_200 = np.array([0,0,0,1.66,51.26,132.44,208.28,271.42,318.49,360.81,386.02,401.24,409.75,413.60,409.71,405.73,394.21,385.43,374.33,360.65])

Ray_AbsorbAl_250 = np.array([0,0,0,0,6.71,120.25,342.16,616.75,901.72,1216.68,1544.41,1850.65,2168.70,2494.73,2826.38,3163.59,3507.13,3857.43,4209.92,4570.23])
Ray_DetectAl_250 = np.array([0,0,0,0,6.22,110.28,308.79,546.68,782.68,1031.81,1277.09,1488.90,1695.19,1888.50,2075.58,2244.53,2402.74,2543.09,2674.84,2792.23])
Ray_AbsorbB_250 = np.array([6.46,20.02,35.48,52.12,62.39,57.29,50.20,43.73,39.42,35.09,31.28,29.31,27.20,25.45,24.18,22.74,21.34,20.25,19.51,18.69])
Ray_DetectB_250 = np.array([6.31,18.53,30.32,40.20,44.17,39.60,34.62,30.26,27.46,24.52,21.93,20.62,19.20,18.00,17.11,16.16,15.15,14.40,13.89,13.31])
Ray_AbsorbN_250 = np.array([20.93,104.03,213.16,337.46,433.07,420.98,380.98,338.88,310.29,279.99,252.02,238.15,222.60,209.80,200.40,189.40,178.77,170.36,164.58,158.39])
Ray_DetectN_250 = np.array([20.56,97.08,184.28,264.23,310.22,293.03,263.87,235.22,216.53,195.82,176.89,167.63,157.25,148.50,141.84,134.60,126.99,121.27,117.17,112.83])
Ray_AbsorbO_250 = np.array([0,0,0,0.03,45.09,256.28,525.12,806.10,1070.06,1350.06,1629.22,1876.31,2129.81,2386.14,2642.44,2899.08,3159.65,3421.79,3681.73,3947.70])
Ray_DetectO_250 = np.array([0,0,0,0.01,13.05,70.58,135.59,193.39,236.27,272.74,299.95,312.80,321.25,323.47,325.21,320.37,314.65,305.52,297.15,287.40])

Ray_AbsorbAl_300 = np.array([0,0,0,0,0.16,51.40,237.16,500.61,798.17,1118.01,1450.67,1766.60,2097.08,2421.39,2751.10,3085.23,3440.02,3786.76,4156.77,4511.40])
Ray_DetectAl_300 = np.array([0,0,0,0,0.14,46.66,212.24,440.35,687.80,941.72,1191.50,1412.55,1629.09,1824.37,2009.32,2174.61,2339.38,2487.92,2623.09,2742.64])
Ray_AbsorbB_300 = np.array([6.45,19.99,35.40,52.13,67.75,69.15,61.65,54.66,48.34,43.19,38.43,35.97,32.96,31.34,29.59,27.85,26.34,25.09,23.42,22.59])
Ray_DetectB_300 = np.array([6.31,18.50,30.27,40.24,46.56,44.98,39.83,35.14,31.30,28.04,25.11,23.62,21.72,20.73,19.60,18.48,17.49,16.68,15.63,15.08])
Ray_AbsorbN_300 = np.array([20.93,103.90,212.72,337.49,462.56,501.64,467.05,422.02,379.68,343.79,309.39,291.68,269.69,257.83,244.81,231.79,220.21,210.80,197.22,191.32])
Ray_DetectN_300 = np.array([20.56,96.94,183.98,264.43,323.28,329.76,302.34,272.56,246.60,223.61,202.42,191.73,177.91,170.60,162.34,153.94,146.36,140.23,132.00,127.78])
Ray_AbsorbO_300 = np.array([0,0,0,0,5.86,141.21,397.79,683.28,971.04,1259.95,1546.76,1805.34,2071.96,2325.97,2580.78,2836.49,3106.53,3365.93,3643.54,3904.00])
Ray_DetectO_300 = np.array([0,0,0,0,1.35,31.22,82.73,132.26,173.21,205.87,229.88,243.64,252.85,256.25,257.16,252.90,248.62,244.13,235.94,230.00])

BeamEnergy = np.arange(1,21,1)


plt.figure(1)
plt.title('B,N,C WDX Intensites (Normalised)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,(L2B/max(L2B)), label = 'B (LDEL2)', marker = 'x', color = 'darkorange')
plt.plot(WDX_Energy,(L2N/max(L2N)), label = 'N (LDEL2)', marker = 'o', color = 'blue')
plt.plot(WDX_Energy,(L1N/max(L1N)), label = 'N (LDEL1)', marker = '^', color = 'navy')
plt.plot(WDX_Energy,(L2C/max(L2C)), label = 'C (LDEL2)', marker = 's', color = 'black')
plt.legend()
plt.xticks(np.arange(5,16,1))

plt.figure(2)
plt.title('Al,O Intensites (Normalised)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,(L1O/max(L1O)), label = 'O (LDEL1)', marker = 'o',color = 'red')
plt.plot(WDX_Energy,(PET_Al/max(PET_Al)), label = 'Al (PETJ)', marker = 'x', color = 'green')
plt.legend()
plt.xticks(np.arange(5,16,1))

plt.figure(4)
plt.title('Nitrogen Intensites by crystal (Normalised)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,(L2N / max(L2N)), label = 'LDEL2', marker = 'o', color = 'blue')
plt.plot(WDX_Energy,(L1N / max(L1N)), label = 'LDEL1', marker = '^', color = 'navy')
plt.legend()
plt.xticks(np.arange(5,16,1))

xGen = np.linspace(0,20,10001)
m, c, r, p, std_err = stats.linregress(EDX_Energy2,EDX_CutOff2_1)
yGen = m * xGen + c

m1, c1, r1, p1, std_err1 = stats.linregress(EDX_Energy2,EDX_CutOff2_10)
yGen1 = m1 * xGen + c1


plt.figure(5)
plt.title('CutOff Energy for EDX')
plt.xlabel('Incident Beam Energy (keV)')
plt.ylabel('Energy where detector reaches CutOff value (keV)')
plt.scatter(EDX_Energy2,EDX_CutOff2_1, label = 'Experemental Data, CutOff set at I_arb = 1')
plt.scatter(EDX_Energy2,EDX_CutOff2_10, label = 'Experemental Data, CutOff set at I_arb = 10')
plt.plot(xGen,yGen, label = 'Line Fit: m = '+str(np.around(m,3))+', c = '+str(np.around(c,3)), linestyle = ':')
plt.plot(xGen,yGen1, label = 'Line Fit:  m = '+str(np.around(m1,3))+', c = '+str(np.around(c1,3)), linestyle = ':')
plt.legend(loc = 'best',fontsize="small")

plt.figure(64)
plt.title('Simulated detection of X-Rays Al,O (250nm)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,Ray_AbsorbAl_250, label = 'I_emit (Al)', marker = 'x', color = 'lime', linestyle = 'dotted')
plt.plot(BeamEnergy,Ray_DetectAl_250, label = 'I_detected (Al)', marker = 'x', color = 'green', linestyle = 'dotted')
plt.plot(BeamEnergy,Ray_AbsorbO_250, label = 'I_emit (O)', marker = 'o', color = 'maroon', linestyle = 'dotted')
plt.plot(BeamEnergy,Ray_DetectO_250, label = 'I_detected (O)', marker = 'o', color = 'red', linestyle = 'dotted')
plt.legend()


plt.figure(74)
plt.title('Simulated detection of X-Rays B,N (250nm)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,Ray_AbsorbB_250, label = 'I_emit (B)', marker = 'x', color = 'darkgoldenrod', linestyle = 'dotted')
plt.plot(BeamEnergy,Ray_DetectB_250, label = 'I_detected (B)', marker = 'x', color = 'darkorange', linestyle = 'dotted')
plt.plot(BeamEnergy,Ray_AbsorbN_250, label = 'I_emit (N)', marker = 'o', color = 'teal', linestyle = 'dotted')
plt.plot(BeamEnergy,Ray_DetectN_250, label = 'I_detected (N)', marker = 'o', color = 'blue', linestyle = 'dotted')
plt.legend()


plt.figure(104)
plt.title('B,N,C Intensities, Simulation (250nm) Vs Experement (Normalised)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectB_250 / max(Ray_DetectB_250)), label = 'I_sim (B)', marker = 'x', color = 'darkorange', linestyle = 'dotted')
plt.plot(BeamEnergy,(Ray_DetectN_250 / max(Ray_DetectN_250)), label = 'I_sim (N)', marker = 'o', color = 'blue', linestyle = 'dotted')
plt.plot(WDX_Energy,(L2N/max(L2N)), label = 'N (LDEL2)', marker = 'o', color = 'blue')
plt.plot(WDX_Energy,(L2B/max(L2B)), label = 'B (LDEL2)', marker = 'x', color = 'darkorange')
plt.plot(WDX_Energy,(L1N / max(L1N)), label = 'N (LDEL1)', marker = '^', color = 'navy')
plt.legend()

AvgDelta = (DeltaEDX10 + DeltaEDX1) / 2
AvgDelta = np.delete(AvgDelta,[0,1,5])


plt.figure(15)
plt.title('Al, O Intensities, Simulation (250nm) Vs Experement (Normalised)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy,(PET_Al/max(PET_Al)), label = 'AL (PETJ)', marker = 'x', color = 'green')
plt.plot(WDX_Energy,(L1O/max(L1O)), label = 'O (LDEL1)', marker = 'x', color = 'red')
plt.plot(BeamEnergy,(Ray_DetectAl_250 / max(Ray_DetectAl_250)), label = 'I_sim (Al)', marker = 'o', color = 'green', linestyle = 'dotted')
plt.plot(BeamEnergy,(Ray_DetectAl_250 / max(Ray_DetectAl_250)), label = 'I_sim (O)', marker = 'o', color = 'red', linestyle = 'dotted')
plt.legend()



plt.figure(131)
plt.title('B,N,C Intensities, Simulation (250nm) Vs Experement (Normalised) (Corrected)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectB_250 / max(Ray_DetectB_250)), label = 'I_sim (B)', marker = 'x', color = 'darkorange', linestyle = 'dotted')
plt.plot(BeamEnergy,(Ray_DetectN_250 / max(Ray_DetectN_250)), label = 'I_sim (N)', marker = 'o', color = 'blue', linestyle = 'dotted')
plt.plot(WDX_Energy-AvgDelta,(L2N/max(L2N)), label = 'N (LDEL2)', marker = 'o', color = 'blue')
plt.plot(WDX_Energy-AvgDelta,(L2B/max(L2B)), label = 'B (LDEL2)', marker = 'x', color = 'darkorange')
plt.plot(WDX_Energy-AvgDelta,(L1N / max(L1N)), label = 'N (LDEL1)', marker = '^', color = 'navy')
plt.legend()

plt.figure(132)
plt.title('Al, O Intensities, Simulation (250nm) Vs Experement (Normalised) (Corrected)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(WDX_Energy-AvgDelta,(PET_Al/max(PET_Al)), label = 'AL (PETJ)', marker = 'x', color = 'green')
plt.plot(WDX_Energy-AvgDelta,(L1O/max(L1O)), label = 'O (LDEL1)', marker = 'x', color = 'red')
plt.plot(BeamEnergy,(Ray_DetectAl_250 / max(Ray_DetectAl_250)), label = 'I_sim (Al)', marker = 'o', color = 'green', linestyle = 'dotted')
plt.plot(BeamEnergy,(Ray_DetectAl_250 / max(Ray_DetectAl_250)), label = 'I_sim (O)', marker = 'o', color = 'red', linestyle = 'dotted')
plt.legend()