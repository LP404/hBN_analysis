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

# def main():
    
    #First set is for WDX
    
DataTable = pd.read_csv('RefData.csv')
path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('hBN first lab.py')) + '\\hBN first lab\\DataSets\\WDX'))

#Note vars()['a'+str(x)] is the 'variable name' 

for x in range(len(files)):
    vars()[str(x)] = np.loadtxt(open(path + "/" + files[x], "rb"), delimiter=",")
    vars()['a'+str(x)] = np.transpose(vars()[str(x)])

List = elementSelect(DataTable)
OFengage, Orders, element = OrderFinder(DataTable)
Orders = Orders/1000

for x in range(len(List)):
    List[x][1] = (List[x][1]/1000)
   
    
for x in range(len(files)):
    plt.figure(x)
    plt.xlabel('Energy (keV)')
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


#Repeat for EDX

path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('hBN first lab.py')) + '\\hBN first lab\\DataSets\\EDX'))

for x in range(len(files)):
    vars()[str(x)] = np.loadtxt(open(path + "/" + files[x], "rb"), delimiter=",")
    vars()['b'+str(x)] = np.transpose(vars()[str(x)])


CutOff = [[] for _ in range(len(files))]

for x in range(len(files)):
    CutOff[x] = np.where((vars()['b'+str(x)][1] > 0) & (vars()['b'+str(x)][1] <= 1))[0]

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
    plt.xticks(np.arange(0, 21, 0.5))
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
                
    # return

# def GuessFunc(x,y,DataTable):
    
#     a = 0
#     GFengage = False
 
#     while a == 0:
#         response = input('Do you wish to initate the guess function? y/n : ')
#         if response.lower() == 'y':
#             a = 1
#             GFengage = True
#         elif response.lower() == 'n':
#             a = 1
#             return
#         else:
#             print('Invalid response.')
            
#     path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('hBN first lab.py')) + '\\hBN first lab\\DataSets\\WDX'))
#     path1, dirs1, files1 = next(os.walk(os.path.dirname(os.path.realpath('hBN first lab.py')) + '\\hBN first lab\\DataSets\\EDX'))
          
#     while b == 0:
#         response = input(' ')
#         if response.lower() == 'y':
#             a = 1
#             GFengage = True
#         elif response.lower() == 'n':
#             a = 1
#             return
#         else:
#             print('Invalid response.')    
    
    
#     for x in range(len(files)):
#         vars()[str(x)] = np.loadtxt(open(path + "/" + files[x], "rb"), delimiter=",")
#         vars()['a'+str(x)] = np.transpose(vars()[str(x)])      
        
#     for x in range(len(files1)):
#         vars()[str(x)] = np.loadtxt(open(path1 + "/" + files1[x], "rb"), delimiter=",")
#         vars()['b'+str(x)] = np.transpose(vars()[str(x)])     
    
#     for x in range(len(files)):
#         vars()['aPolyX'+str(x)] = np.linspace(min(vars()['a'+str(x)][0]),max(vars()['a'+str(x)][0]),1001)
#         vars()['aPolyY'+str(x)] = np.poly1d(np.polyfit(vars()['a'+str(x)][0],vars()['a'+str(x)][1],20))

#     for x in range(len(files1)):
#         vars()['bPolyX'+str(x)] = np.linspace(min(vars()['b'+str(x)][0]),max(vars()['b'+str(x)][0]),1001)
#         vars()['bPolyY'+str(x)] = np.poly1d(np.polyfit(vars()['b'+str(x)][0],vars()['b'+str(x)][1],20))
        
        
    
#     MaxPointLocA = np.array([])
#     MaxPointLocB = np.array([])
#     MinPointLocA = np.array([])
#     MinPointLocB = np.array([])
    
    
#     for x in range(len(files)):
#         for y in range(1,(len(vars()['aPolyX'+str(x)])-1)):
#             if ((vars()['aPolyY'+str(x)] - vars()['aPolyY'+str((x-1))]) / (vars()['aPolyX'+str(x)] - vars()['aPolyX'+str((x-1))])) > 0 and ((vars()['aPolyY'+str((x+1))] - vars()['aPolyY'+str(x)]) / (vars()['aPolyX'+str((x+1))] - vars()['aPolyX'+str(x)]))  < 0:
#                 MaxPointLocA = np.append(MaxPointLocA,[vars()['aPolyX'+str(x)]])
                
#     for x in range(len(files1)):
#         for y in range(1,(len(vars()['bPolyX'+str(x)])-1)):
#             if ((vars()['bPolyY'+str(x)] - vars()['bPolyY'+str((x-1))]) / (vars()['bPolyX'+str(x)] - vars()['bPolyX'+str((x-1))])) > 0 and ((vars()['bPolyY'+str((x+1))] - vars()['bPolyY'+str(x)]) / (vars()['bPolyX'+str((x+1))] - vars()['bPolyX'+str(x)]))  < 0:
#                 MaxPointLocB = np.append(MaxPointLocB,[vars()['bPolyX'+str(x)]])
                
#     for x in range(len(files)):
#         for y in range(1,(len(vars()['aPolyX'+str(x)])-1)):
#             if ((vars()['aPolyY'+str(x)] - vars()['aPolyY'+str((x-1))]) / (vars()['aPolyX'+str(x)] - vars()['aPolyX'+str((x-1))])) < 0 and ((vars()['aPolyY'+str((x+1))] - vars()['aPolyY'+str(x)]) / (vars()['aPolyX'+str((x+1))] - vars()['aPolyX'+str(x)]))  > 0:
#                 MinPointLocA = np.append(MinPointLocA,[vars()['aPolyX'+str(x)]])
                
#     for x in range(len(files1)):
#         for y in range(1,(len(vars()['bPolyX'+str(x)])-1)):
#             if ((vars()['bPolyY'+str(x)] - vars()['bPolyY'+str((x-1))]) / (vars()['bPolyX'+str(x)] - vars()['bPolyX'+str((x-1))])) < 0 and ((vars()['bPolyY'+str((x+1))] - vars()['bPolyY'+str(x)]) / (vars()['bPolyX'+str((x+1))] - vars()['bPolyX'+str(x)]))  > 0:
#                 MinPointLocB = np.append(MinPointLocB,[vars()['bPolyX'+str(x)]])
                
    
#     if min(MaxPointLocA) < min(MinPointLocA):
#         MinMaxMin = False
#     else:
#         MinMaxMin = True
        
#     if MinMaxMin = True:
#         MinLockPointA = np.append(MinLockPointA,)
#         for x in range(len(MaxLocPointA)):
            
        
    
    
    
#     #Compare array values to find out if the min or max is first
#     #Seperate Graph accordingly
#     #Take each sector and find closes element line to the midpoint
#     #Perhaps look for a second or third order, compare the delta
#     #If the delta is less than the delta of the seperate line assign second order line
#     #Add ability to specifiy line for graphing
#     #Find max value in that sector and call it ExpPeak
    
    
#     #New function that overrides all functions that plots pecific graphs.
#     #Gather peak values.
#     #
                

                
    
#     Out = DataTable[DataTable['Element'].str.endswith(element)]
    
#     xp = np.linspace(min(a1[0]),max(a1[0]),1001)
#     p30 = np.poly1d(np.polyfit(a1[0],a1[1],20))
    
#     return

# if __name__ == '__main__':
#     main()