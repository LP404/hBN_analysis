import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# LV_EDX_Cut1 = np.array([5.78,5.85,5.74,6.42,6.59,6.88,6.89,6.73,7.84,7.8,7.27,8.63,9.7,9.7,8.11,8.87,11.45,11.39,8.95,10.79,14.09,13.56,14.15,14.17,10.63,18.9])

# LV_EDX_Cut10 = np.array([5.44,5.59,5.46,5.91,6.1,6.57,6.62,6.41,7.47,7.46,6.87,7.85,9.16,9.13,7.52,8.19,10.68,10.67,8.1,9.9,12.99,12.11,12.91,12.81,9.67,16.19])

# LV_EDX_Energy = np.array([6,7,8,10,12,15,20])
# EDX_Energy = np.array([6,7,8,10,12,15])

# LV_EDXPeaksN = np.array([1070, 1684, 1776, 1394, 1196, 1824, 1946, 2161, 1488, 1625, 2749, 1478,  985, 1168, 1596, 1456,  793,  750, 1659, 1316,  545,  336, 558,  574, 1544, 1317])

# LV_EDXPeaksO = np.array([20233, 27400, 25015, 21065, 21420, 40288, 40200, 44746, 37999, 37284, 49877, 35953, 33453, 34466, 40839, 34212, 28113, 28278,35933, 33768, 23975, 12857, 21404, 21959, 35618, 38393])

# LV_EDXPeaksAl = np.array([17986, 24891, 22544, 19563, 21418, 41854, 40806, 42961, 44682, 43452, 51782, 42887, 48815, 49315, 45000, 41782, 49619, 49066, 42351, 45196, 54057, 30174, 50354, 49236, 44549, 47074])

EDX_Energy = np.array([6,7,8,10,12,15,20])
LV_EDX_Energy = np.array([6,7,8,10,12,15])

EDX_Cut1 = np.array([5.74,6.59,7.27,8.63,8.87,10.79,18.9])
LV_EDX_Cut1_100 = np.array([5.78,6.88,7.84,9.7,11.45,14.09])
LV_EDX_Cut1_30 = np.array([5.85,6.89,7.8,9.7,11.39,14.15])

EDX_Cut10 = np.array([5.46,6.1,6.87,7.85,8.19,9.9,16.19])
LV_EDX_Cut10_100 = np.array([5.44,6.57,7.47,9.16,10.68,12.99])
LV_EDX_Cut10_30 = np.array([5.59,6.62,7.46,9.13,10.67,12.91])

EDXPeaksN = np.array([1776,1196,2749,1478,1456,1316,1317])
LV_EDXPeaksN_100 = np.array([1070,1824,1488,985,793,545])
LV_EDXPeaksN_30 = np.array([1684,1946,1625,1168,750,558])

EDXPeaksO = np.array([25015,21420,49877,35953,34212,33768,38393])
LV_EDXPeaksO_100 = np.array([20233,40288,37999,33453,28113,23975])
LV_EDXPeaksO_30 = np.array([27400,40200,37284,34466,28278,21404])

EDXPeaksAl = np.array([22544,21418,42961,42887,41782,45196,47074])
LV_EDXPeaksAl_100 = np.array([17986,41854,44682,48815,49619,54057])
LV_EDXPeaksAl_30 = np.array([24891,40806,43452,49315,49066,50354])

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

Ray_AbsorbAl_350 = np.array([0,0,0,0,0.15,50.51,235.56,496.81,794.68,796.01,1450.13,1771.30,2095.44,2423.62,2750.91,3087.47,3444.53,3789.35,4147.64,4524.84])
Ray_DetectAl_350 = np.array([0,0,0,0,0.14,45.84,210.87,436.98,684.76,685.95,1191.60,1415.79,1627.75,1824.53,2006.22,2177.48,2345.46,2486.88,2620.23,2750.88])
Ray_AbsorbB_350 = np.array([6.46,20.04,35.49,52.03,67.91,69.34,62.38,55.02,48.60,43.37,38.64,35.58,32.95,30.89,29.30,28.07,26.19,24.85,23.75,22.24])
Ray_DetectB_350 = np.array([6.31,18.56,30.32,40.12,46.69,45.16,40.07,35.47,31.43,28.12,25.27,23.35,21.70,20.41,19.44,18.61,17.43,16.56,15.83,14.86])
Ray_AbsorbN_350 = np.array([20.93,104.16,213.18,336.90,463.66,502.78,469.92,424.66,381.48,344.91,310.77,288.83,269.71,254.47,242.70,233.65,218.98,210.30,200.22,188.59])
Ray_DetectN_350 = np.array([20.56,97.22,184.24,263.76,324.13,330.93,303.90,274.99,247.45,224.13,203.48,189.80,177.81,168.33,161.13,154.99,145.76,140.15,133.49,125.99])
Ray_AbsorbO_350 = np.array([0,0,0,0,5.76,138.68,394.68,678.69,966.34,1258.05,1545.89,1810.49,2070.94,2329.51,2581.46,2838.26,3110.30,3368.37,3634.48,3916.41])
Ray_DetectO_350 = np.array([0,0,0,0,1.33,30.65,82.21,131.43,172.37,206.13,230.21,244.01,252.63,255.87,255.78,253.46,249.95,243.17,236.72,230.45])

Ray_AbsorbAl_400 = np.array([0,0,0,0,0,1.54,75.78,281.37,570.58,892.09,1248.95,1589.41,1919.96,2263.37,2592.61,2943.50,3298.31,3657.69,4021.60,4377.66])
Ray_DetectAl_400 = np.array([0,0,0,0,0,1.37,66.57,84.54,243.41,484.42,741.28,1013.20,1254.67,1472.08,1686.67,1868.44,2048.60,2217.51,2371.64,2509.01,2625.72])
Ray_AbsorbB_400 = np.array([6.44,20.00,35.54,52.09,69.11,84.07,48.30,77.60,68.71,62.17,54.90,49.83,46.41,43.25,40.82,38.56,35.99,34.13,32.31,31.01])
Ray_DetectB_400 = np.array([6.30,18.52,30.26,40.18,47.21,50.93,43.48,38.51,34.88,30.95,28.43,26.63,24.94,23.69,22.44,21.07,19.95,19.02,18.25])
Ray_AbsorbN_400 = np.array([20.88,103.95,213.48,337.26,469.12,594.38,626.10,592.50,536.14,491.77,439.55,403.05,378.41,354.99,337.10,319.99,300.54,286.15,272.35,262.18])
Ray_DetectN_400 = np.array([20.52,97.02,184.49,264.03,326.55,366.99,362.29,334.92,302.33,277.14,248.63,230.40,217.50,205.04,165.87,186.48,176.14,167.48,160.36,154.40])
Ray_AbsorbO_400 = np.array([0,0,0,0,0.01,13.82,169.13,432.96,739.59,1043.86,1364.65,1652.85,1922.22,2196.78,2451.95,2723.13,2994.09,3265.29,3537.68,3800.54])
Ray_DetectO_400 = np.array([0,0,0,0,0,1.95,22.68,54.36,86.04,111.58,133.18,145.85,153.02,158.72,158.77,157.79,156.27,153.28,148.87,144.16])


Ray_DetectN_450 = np.array([20.56,97.25,184.41,264.40,326.80,369.96,381.05,357.42,326.88,295.17,266.69,246.80,232.66,221.72,209.18,201.99,189.70,180.38,173.44,166.69])


BeamEnergy = np.arange(1,21,1)


plt.figure(1)
plt.title('EDX Intensites (Normalised)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(EDX_Energy,(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot(EDX_Energy,(EDXPeaksO/max(EDXPeaksO)), label = 'O', marker = 'o')
plt.plot(EDX_Energy,(EDXPeaksAl/max(EDXPeaksAl)), label = 'Al', marker = 's')
plt.legend()
plt.xticks(np.arange(6,20,1))

plt.figure(2)
plt.title('LV-EDX Intensites (30Pa) (Normalised)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N', marker = 'x')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksO_30/max(LV_EDXPeaksO_30)), label = 'O', marker = 'o')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksAl_30/max(LV_EDXPeaksAl_30)), label = 'Al', marker = 's')
plt.legend()
plt.xticks(np.arange(6,20,1))

plt.figure(3)
plt.title('LV-EDX Intensites (100Pa) (Normalised)')
plt.xlabel('Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N', marker = 'x')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksO_100/max(LV_EDXPeaksO_100)), label = 'O', marker = 'o')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksAl_100/max(LV_EDXPeaksAl_100)), label = 'Al', marker = 's')
plt.legend()
plt.xticks(np.arange(6,20,1))

xGen = np.linspace(0,20,10001)
m, c, r, p, std_err = stats.linregress(EDX_Energy,EDX_Cut1)
dm = m * np.sqrt((1-r)/(len(EDX_Energy)-2)) #?
m1, c1, r1, p1, std_err1 = stats.linregress(LV_EDX_Energy,LV_EDX_Cut1_30)
m2, c2, r2, p2, std_err2 = stats.linregress(LV_EDX_Energy,LV_EDX_Cut1_100)
m3, c3, r3, p3, std_err3 = stats.linregress(EDX_Energy,EDX_Cut10)
m4, c4, r4, p4, std_err4 = stats.linregress(LV_EDX_Energy,LV_EDX_Cut10_30)
m5, c5, r5, p5, std_err5 = stats.linregress(LV_EDX_Energy,LV_EDX_Cut10_100)

yGen = m * xGen + c
yGen1 = m1 * xGen + c1
yGen2 = m2 * xGen + c2
yGen3 = m3 * xGen + c3
yGen4 = m4 * xGen + c4
yGen5 = m5 * xGen + c5


plt.figure(5)
plt.title('CutOff Energy for EDX (No Vaccum)')
plt.xlabel('Incident Beam Energy (keV)')
plt.ylabel('Energy where detector reaches CutOff value (keV)')
plt.scatter(EDX_Energy,EDX_Cut1, label = 'Experemental Data, CutOff set at I_arb = 1')
plt.scatter(EDX_Energy,EDX_Cut10, label = 'Experemental Data, CutOff set at I_arb = 10')
plt.plot(xGen,yGen, label = 'Line Fit: m = '+str(np.around(m,3)) + '±' + str(np.around(std_err,3)) +', c = '+str(np.around(c,3)), linestyle = ':')
plt.plot(xGen,yGen3, label = 'Line Fit:  m = '+str(np.around(m3,3)) + '±' + str(np.around(std_err3,3)) + ', c = '+str(np.around(c3,3)), linestyle = ':')
plt.legend(loc = 'best',fontsize="small")

plt.figure(6)
plt.title('CutOff Energy for EDX (LV 30Pa)')
plt.xlabel('Incident Beam Energy (keV)')
plt.ylabel('Energy where detector reaches CutOff value (keV)')
plt.scatter(LV_EDX_Energy,LV_EDX_Cut1_30, label = 'Experemental Data, CutOff set at I_arb = 1')
plt.scatter(LV_EDX_Energy,LV_EDX_Cut10_30, label = 'Experemental Data, CutOff set at I_arb = 10')
plt.plot(xGen,yGen1, label = 'Line Fit: m = '+str(np.around(m1,3)) + '±' + str(np.around(std_err1,3)) +', c = '+str(np.around(c1,3)), linestyle = ':')
plt.plot(xGen,yGen4, label = 'Line Fit:  m = '+str(np.around(m4,3)) + '±' + str(np.around(std_err4,3)) +', c = '+str(np.around(c4,3)), linestyle = ':')
plt.legend(loc = 'best',fontsize="small")

plt.figure(7)
plt.title('CutOff Energy for EDX (LV 100Pa)')
plt.xlabel('Incident Beam Energy (keV)')
plt.ylabel('Energy where detector reaches CutOff value (keV)')
plt.scatter(LV_EDX_Energy,LV_EDX_Cut1_100, label = 'Experemental Data, CutOff set at I_arb = 1')
plt.scatter(LV_EDX_Energy,LV_EDX_Cut10_100, label = 'Experemental Data, CutOff set at I_arb = 10')
plt.plot(xGen,yGen2, label = 'Line Fit: m = '+str(np.around(m2,3)) + '±' + str(np.around(std_err2,3)) +', c = '+str(np.around(c2,3)), linestyle = ':')
plt.plot(xGen,yGen5, label = 'Line Fit:  m = '+str(np.around(m5,3)) + '±' + str(np.around(std_err,5)) +', c = '+str(np.around(c5,3)), linestyle = ':')
plt.legend(loc = 'best',fontsize="small")

plt.figure(103)
plt.title('Detection of X-Rays, Simulation (200nm) Vs Experement (Normalised)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_200 / max(Ray_DetectN_200)), label = 'I_sim (N)', marker = 'o')
plt.plot(EDX_Energy,(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()

plt.figure(104)
plt.title('Detection of X-Rays, Simulation (250nm) Vs Experement (Normalised)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_250 / max(Ray_DetectN_250)), label = 'I_sim (N)', marker = 'o')
plt.plot(EDX_Energy,(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot(LV_EDX_Energy,(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()


DeltaEDX1 = EDX_Energy - EDX_Cut1
DeltaEDX10 = EDX_Energy - EDX_Cut10

LV_DeltaEDX1_100 = LV_EDX_Energy - LV_EDX_Cut1_100
LV_DeltaEDX10_100 = LV_EDX_Energy - LV_EDX_Cut10_100

LV_DeltaEDX1_30 = LV_EDX_Energy - LV_EDX_Cut1_30
LV_DeltaEDX10_30 = LV_EDX_Energy - LV_EDX_Cut10_30

AvgDelta = (DeltaEDX10 + DeltaEDX1) / 2
AvgDelta_LV_100 = (LV_DeltaEDX10_100 + LV_DeltaEDX1_100) / 2
AvgDelta_LV_30 = (LV_DeltaEDX10_30 + LV_DeltaEDX1_30) / 2



plt.figure(130)
plt.title('Detection of X-Rays, Simulation (200nm) Vs Experement (Normalised) (Overlayed)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_200 / max(Ray_DetectN_200)), label = 'I_sim (N)', marker = 'o')
plt.plot((EDX_Energy - AvgDelta),(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot((LV_EDX_Energy - AvgDelta_LV_30),(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot((LV_EDX_Energy - AvgDelta_LV_100),(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()

plt.figure(131)
plt.title('Detection of X-Rays, Simulation (250nm) Vs Experement (Normalised) (Overlayed)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_250 / max(Ray_DetectN_250)), label = 'I_sim (N)', marker = 'o')
plt.plot((EDX_Energy - AvgDelta),(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot((LV_EDX_Energy - AvgDelta_LV_30),(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot((LV_EDX_Energy - AvgDelta_LV_100),(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()

plt.figure(132)
plt.title('Detection of X-Rays, Simulation (300nm) Vs Experement (Normalised) (Overlayed)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_300 / max(Ray_DetectN_300)), label = 'I_sim (N)', marker = 'o')
plt.plot((EDX_Energy - AvgDelta),(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot((LV_EDX_Energy - AvgDelta_LV_30),(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot((LV_EDX_Energy - AvgDelta_LV_100),(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()

plt.figure(133)
plt.title('Detection of X-Rays, Simulation (350nm) Vs Experement (Normalised) (Overlayed)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_350 / max(Ray_DetectN_350)), label = 'I_sim (N)', marker = 'o')
plt.plot((EDX_Energy - AvgDelta),(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot((LV_EDX_Energy - AvgDelta_LV_30),(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot((LV_EDX_Energy - AvgDelta_LV_100),(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()

plt.figure(134)
plt.title('Detection of X-Rays, Simulation (400nm) Vs Experement (Normalised) (Overlayed)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_400 / max(Ray_DetectN_400)), label = 'I_sim (N)', marker = 'o')
plt.plot((EDX_Energy - AvgDelta),(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot((LV_EDX_Energy - AvgDelta_LV_30),(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot((LV_EDX_Energy - AvgDelta_LV_100),(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()

plt.figure(135)
plt.title('Detection of X-Rays, Simulation (450nm) Vs Experement (Normalised) (Overlayed)')
plt.xlabel('Beam Energy (keV)')
plt.ylabel('Intensity (Arb. Units)')
plt.plot(BeamEnergy,(Ray_DetectN_450 / max(Ray_DetectN_450)), label = 'I_sim (N)', marker = 'o')
plt.plot((EDX_Energy - AvgDelta),(EDXPeaksN/max(EDXPeaksN)), label = 'N', marker = 'x')
plt.plot((LV_EDX_Energy - AvgDelta_LV_30),(LV_EDXPeaksN_30/max(LV_EDXPeaksN_30)), label = 'N (30Pa)', marker = 'o')
plt.plot((LV_EDX_Energy - AvgDelta_LV_100),(LV_EDXPeaksN_100/max(LV_EDXPeaksN_100)), label = 'N (100Pa)', marker = 's')
plt.legend()