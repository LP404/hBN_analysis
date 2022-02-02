import numpy as np
import matplotlib.pyplot as plt


done = False
xVals = np.array([])
yVals = np.array([])
counter = 0

while done == False:
    counter += 1
    xVal = float(input('Please input the value of the electron beam energy (in keV) for index №' +str(counter)+' ' ))
    yVal = float(input('Please input the value of the cutoff energy (in keV) for index №' +str(counter)+' ' ))
    xVals = np.append(xVals,xVal)
    yVals = np.append(yVals,yVal)
    AskIfDone = input('Are you finished inputting the values? y/n : ')
    if AskIfDone.lower() == 'y':
        done = True
    elif AskIfDone.lower() == 'n':
        pass
    else:
        print('Invalid response.')
        
        
print(xVals)