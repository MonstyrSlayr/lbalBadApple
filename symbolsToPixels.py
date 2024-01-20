#takes the symbols and converts them into 1s and 0s

import cv2 as cv
import os
import numpy as np

symbolDict = {}

imgDirectory = os.fsencode("img")

for file in os.listdir(imgDirectory):
    filename = "img/" + os.fsdecode(file)
    
    symbol = cv.imread(filename, cv.IMREAD_UNCHANGED)
    symbolString = ""
    
    for j in range(len(symbol)):
        for i in range(len(symbol[j])):
            col = symbol[j][i]
            #print(col)
            
            if (col[3] == 0):
                symbolString += "1" #transparent
            else:
                symbolString += "0" #opaque

    symbolDict[filename] = symbolString

np.save('symbolData.npy', symbolDict)