import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rand
import os

def elementSelect(DataTable):
    
    num = input("How many elements will the data be compared against? : ")
    
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

def OrderFinder(DataTable):
    a = 0
    OFengage = False
    
    while a == 0:
        response = input('Do you wish to check for nth orders? y/n : ')
        if response.lower() == 'y':
            a = 1
            OFengage = True
        elif response.lower() == 'n':
            a = 1
            return OFengage, np.array([0]), 'null'
        else:
            print('Invalid response.')
    
    element = input('Enter chemical symbol of the element : ')
    print(DataTable[DataTable['Element'].str.endswith(element)])
    loc = input('Enter Index of the energy of element line that will be examined : ')
    energy_01 = DataTable.iloc[int(loc)][0]
    OrderEnergy = np.zeros(5)
    for x in range(len(OrderEnergy)):
        OrderEnergy[x] = energy_01 / (x+1)
    
    return OFengage, OrderEnergy, element

path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('hBN second lab.py')) + '\\hBN second lab\\CSVs2'))

for x in range(len(files)):
    vars()[str(x)] = np.loadtxt(open(path + "/" + files[x], "rb"), delimiter=",")
    vars()['b'+str(x)] = np.transpose(vars()[str(x)])

DataTable = pd.read_csv('RefData.csv')
List = elementSelect(DataTable)
OFengage, Orders, element = OrderFinder(DataTable)
Orders = Orders/1000

for x in range(len(List)):
    List[x][1] = (List[x][1]/1000)


CutOff = [[] for _ in range(len(files))]

#Cutt = np.array([2,3,3,5,7,7,7,10,12,15,15,15])
Cutt = np.array([6,6,6,7,7,7,7,7,8,8,8,10,10,10,10,12,12,12,12,15,15,15,15,15,15,20])

#Cut1 = np.array([5.78,5.85,5.74,6.42,6.59,6.88,6.89,6.73,7.84,7.8,7.27,8.63,9.7,9.7,8.11,8.87,11.45,11.39,8.95,10.79,14.09,13.56,14.15,14.17,10.63,18.9])
#Cut10 = np.array([5.44,5.59,5.46,5.91,6.1,6.57,6.62,6.41,7.47,7.46,6.87,7.85,9.16,9.13,7.52,8.19,10.68,10.67,8.1,9.9,12.99,12.11,12.91,12.81,9.67,16.19])

for x in range(len(files)):
    CutOff[x] = np.where(vars()['b'+str(x)][1] > -1 & (vars()['b'+str(x)][0] <= Cutt[x]))[0]
    #CutOff[x] = np.where((vars()['b'+str(x)][1] > 0) & (vars()['b'+str(x)][1] <= 1) & (vars()['b'+str(x)][0] <= Cutt[x]))[0]
    
# CuffOff1 = np.array([1.95,2.95,2.99,4.28,4.36,4.40,4.23,5.38,6.29,8.27,8.53,7.74])
# CuffOff10 = np.array([1.90,2.88,2.90,4.06,4.02,4.15,3.82,4.86,5.62,7.12,6.95,6.87])

for x in range(len(files)):
    vars()['bb'+str(x)] = np.zeros((2,len(CutOff[x])))
    
    for y in range(0,2):
        for z in range(len(CutOff[x])):
            vars()['bb'+str(x)][y][z] = vars()['b'+str(x)][y][CutOff[x][z]]
    

for x in range(len(files)):
    plt.figure((48751*(x+1)))
    plt.xlabel('Energy (keV)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title(files[x])
    plt.semilogy(vars()['bb'+str(x)][0],vars()['bb'+str(x)][1],zorder = 0)
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(vars()['bb'+str(x)][0]) and List[y][1][z] >= min(vars()['bb'+str(x)][0]) :
                plt.vlines(x=List[y][1][z],ymin = 0, ymax = ((max(vars()['bb'+str(x)][1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(vars()['bb'+str(x)][1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    for z in range(len(Orders)):    
        if OFengage == True and Orders[z] <= max(vars()['bb'+str(x)][0]) and Orders[z] >= min(vars()['bb'+str(x)][0]) :
            plt.vlines(x=Orders[z],ymin = 0, ymax = ((max(vars()['bb'+str(x)][1]) * Orders[z]) / max(Orders)), color = 'grey',ls=':', lw=2, zorder=20)
            plt.text(Orders[z],((max(vars()['bb'+str(x)][1]) * Orders[z]) / max(Orders)), element + ' Order ' + str(z+1))