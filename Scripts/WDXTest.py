import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rand
import os

DataTable1 = pd.read_csv('RefData.csv')

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
            return OrderFinder, np.array([0]), 'null'
        else:
            print('Invallid response.')
    
    element = input('Enter chemical symbol of the element : ')
    print(DataTable[DataTable['Element'].str.endswith(element)])
    loc = input('Enter Index of the energy of element line that will be examined : ')
    energy_01 = DataTable.iloc[int(loc)][0]
    OrderEnergy = np.zeros(5)
    for x in range(len(OrderEnergy)):
        OrderEnergy[x] = energy_01 / (x+1)
    
    return OFengage, OrderEnergy, element
    

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
    OFengage, Orders, element = OrderFinder(DataTable)
    Orders = Orders/1000
    
    for x in range(len(List)):
        List[x][1] = (List[x][1]/1000)
    
    
    plt.figure(0)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('TAPH Data')
    plt.plot(a1[0],a1[1],zorder = 0)
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(a1[0]) and List[y][1][z] >= min(a1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0, ymax = ((max(a1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(a1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    for z in range(len(Orders)):    
        if OFengage == True and Orders[z] <= max(a1[0]) and Orders[z] >= min(a1[0]) :
            plt.vlines(x=Orders[z],ymin = 0, ymax = ((max(a1[1]) * Orders[z]) / max(Orders)), color = 'grey',ls=':', lw=2, zorder=20)
            plt.text(Orders[z],((max(a1[1]) * Orders[z]) / max(Orders)), element + ' Order ' + str(z+1))
        
    
    plt.figure(1)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('LDE1L Data')
    plt.plot(b1[0],b1[1],zorder = 0) 
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(b1[0]) and List[y][1][z] >= min(b1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0,ymax = ((max(b1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(b1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    for z in range(len(Orders)):
        if OFengage == True and Orders[z] <= max(b1[0]) and Orders[z] >= min(b1[0]) :
            plt.vlines(x=Orders[z],ymin = 0, ymax = ((max(b1[1]) * Orders[z]) / max(Orders)), color = 'grey',ls=':', lw=2, zorder=20)
            plt.text(Orders[z],((max(b1[1]) * Orders[z]) / max(Orders)), element + ' Order ' + str(z+1))
       
    
    plt.figure(2)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('PETJ Data')
    plt.plot(c1[0],c1[1],zorder = 0)
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(c1[0]) and List[y][1][z] >= min(c1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0,ymax = ((max(c1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(c1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    for z in range(len(Orders)):
        if OFengage == True and Orders[z] <= max(c1[0]) and Orders[z] >= min(c1[0]) :
            plt.vlines(x=Orders[z],ymin = 0, ymax = ((max(c1[1]) * Orders[z]) / max(Orders)), color = 'grey',ls=':', lw=2, zorder=20)
            plt.text(Orders[z],((max(c1[1]) * Orders[z]) / max(Orders)), element + ' Order ' + str(z+1))
    
    plt.figure(3)
    plt.xlabel('Energy (kEv)')
    plt.ylabel('Intensity (Arb. Units)')
    plt.title('LIFH Data')
    plt.plot(d1[0],d1[1],zorder = 0)
    for y in range(len(List)):
        for z in range(len(List[y][1])):
            if List[y][1][z] <= max(d1[0]) and List[y][1][z] >= min(d1[0]) :
                plt.vlines(x=List[y][1][z],ymin = 0,ymax = ((max(d1[1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                plt.text(List[y][1][z],((max(d1[1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
    for z in range(len(Orders)):
        if OFengage == True and Orders[z] <= max(d1[0]) and Orders[z] >= min(d1[0]) :
            plt.vlines(x=Orders[z],ymin = 0, ymax = ((max(a1[1]) * Orders[z]) / max(Orders)), color = 'grey',ls=':', lw=2, zorder=20)
            plt.text(Orders[z],((max(d1[1]) * Orders[z]) / max(Orders)), element + ' Order ' + str(z+1))
    
    
    
    return

def main1():
    
    #First set is for WDX
    
    DataTable = pd.read_csv('RefData.csv')
    path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('WDXTest.py')) + '\\hBN first lab\\DataSets\\WDX'))
    path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('hBN first lab.py'))+ '\\hBN first lab\\DataSets\\WDX'))
    
    
    #Note vars()['a'+str(x)] is the 'variable name' 
    
    for x in range(len(files)):
        vars()[str(x)] = np.loadtxt(open(path + "/" + files[x], "rb"), delimiter=",")
        vars()['a'+str(x)] = np.transpose(vars()[str(x)])
    
    List = elementSelect(DataTable)
    OFengage, Orders, element = OrderFinder(DataTable)
    Orders = Orders/1000
    
    for x in range(len(List)):
        List[x][1] = (List[x][1]/1000)
       
        
    #LDE2L
    #LDE1L
    #PETJ
    #TAP
    
    for x in range(len(files)):
        plt.figure(x)
        plt.xlabel('Energy (kEv)')
        plt.ylabel('Intensity (Arb. Units)')
        plt.title(files[x])
        plt.plot(vars()['a'+str(x)][0],vars()['a'+str(x)][1],zorder = 0)
        for y in range(len(List)):
            for z in range(len(List[y][1])):
                if List[y][1][z] <= max(vars()['a'+str(x)][0]) and List[y][1][z] >= min(vars()['a'+str(x)][0]) :
                    plt.vlines(x=List[y][1][z],ymin = 0, ymax = ((max(vars()['a'+str(x)][1]) * List[y][3][z]) / max(List[y][3])), color = (List[y][4][0],List[y][4][1],List[y][4][2]),ls=':', lw=2, zorder=10)
                    plt.text(List[y][1][z],((max(vars()['a'+str(x)][1]) * List[y][3][z]) / max(List[y][3])), List[y][0] + ' ' + List[y][2][z])
        for z in range(len(Orders)):    
            if OFengage == True and Orders[z] <= max(vars()['a'+str(x)][0]) and Orders[z] >= min(vars()['a'+str(x)][0]) :
                plt.vlines(x=Orders[z],ymin = 0, ymax = ((max(vars()['a'+str(x)][1]) * Orders[z]) / max(Orders)), color = 'grey',ls=':', lw=2, zorder=20)
                plt.text(Orders[z],((max(vars()['a'+str(x)][1]) * Orders[z]) / max(Orders)), element + ' Order ' + str(z+1))

    return


if __name__ == '__main__':
    main1()

#TODO
#Monoschromiter, read up into
#Look into phases of G2O3
#AlGAO, aluminium potential
#Corunium crystal strucutre 