# takes the symbols in /symbols and converts them into 1s and 0s, and shoves them into symbolData.npy

import cv2 as cv
import os
import numpy as np

symbolDict = {}

imgDirectory = os.fsencode("symbols")

for file in os.listdir(imgDirectory):
    filename = "symbols/" + os.fsdecode(file)
    
    symbol = cv.imread(filename, cv.IMREAD_UNCHANGED)
    symbolString = ""
    
    for j in range(len(symbol)):
        for i in range(len(symbol[j])):
            col = symbol[j][i]
            
            if (col[3] == 0):
                symbolString += "0" # transparent
            else:
                symbolString += "1" # opaque

    symbolDict[filename] = symbolString

np.save('symbolData.npy', symbolDict)