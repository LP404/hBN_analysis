import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rand

def elementSelect(DataTable):
    
    num = input("How many elements will the data be comapred against? : ")
    
    num = int(num)
    
    BigList = [[0,0,0,0,[rand.randint(0,256)/256,rand.randint(0,256)/256,rand.randint(0,256)/256]] for _ in range(num)]
    
    for y in range(0,num):    
        
        element = input('Enter chemical symbol of element № ' + str((y+1)) + ' : ')    
    
        Out = DataTable[DataTable['Element'].str.endswith(element)]
        
        OutL = Out.values.tolist()
    
        energy = np.zeros(len(OutL))
        line = list()
        intensity = np.zeros(len(OutL))
        
        for x in range(len(OutL)):
            energy[x] = float(OutL[x][0])
            line.append(str(OutL[x][2]))
            intensity[x] = int(OutL[x][3])
            
        BigList[y][0] = element
        BigList[y][1] = energy
        BigList[y][2] = line
        BigList[y][3] = intensity
        
     
    return BigList


# Designed this to smooth out PETJ, didn't work. 
# c2 = c1[1][:]
# c2 = np.array_split(c2,(len(c2)/10))
# for x in range(len(c2)):
#     avg = np.average(c2[x])
#     for y in range(len(c2[x])):
#         if (c2[x][y]/avg) >= 1.5:
#             pass
#         else:
#             c2[x][y] = avg
# c2 = np.block(c2)

#Note to self List[Element][Index for array/list][Value in array/list]
# 0 = Element, 1 = energy, 2 = line, 3 = intensity, 4 = RGB code


def main():

    DataTable = pd.read_csv('RefData.csv')
    a = np.loadtxt(open("CH-1 TAPH.csv", "rb"), delimiter=",")
    b = np.loadtxt(open("CH-2 LDE1L.csv", "rb"), delimiter=",")
    c = np.loadtxt(open("CH-3 PETJ.csv", "rb"), delimiter=",")
    d = np.loadtxt(open("CH-4 LIFH.csv", "rb"), delimiter=",")
    
    a1 = np.transpose(a)
    b1 = np.transpose(b)
    c1 = np.transpose(c)
    d1 = np.transpose(d)
    
    List = elementSelect(DataTable)
    
    for x in range(len(List)):
        List[x][1] = (List[x][1]/1000)
    
    
    plt.figure(0)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('TAPH Data')
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(a1[0]) and List[y][1][z] >= min(a1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0, ymax = ((max(a1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(a1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    plt.plot(a1[0],a1[1],zorder = 0)
        
    
    plt.figure(1)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('LDE1L Data')
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(b1[0]) and List[y][1][z] >= min(b1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0,ymax = ((max(b1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(b1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    plt.plot(b1[0],b1[1],zorder = 0)    
    
    plt.figure(2)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('PETJ Data')
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(c1[0]) and List[y][1][z] >= min(c1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0,ymax = ((max(c1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(c1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    plt.plot(c1[0],c1[1],zorder = 0)
    
    plt.figure(3)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('LIFH Data')
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(d1[0]) and List[y][1][z] >= min(d1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0,ymax = ((max(d1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(d1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    plt.plot(d1[0],d1[1],zorder = 0)
    
    
    
    return

if __name__ == '__main__':
    main()

#TODO
#Monoschromiter, read up into
#Look into phases of G2O3
#AlGAO, aluminium potential
#Corunium crystal strucutre 