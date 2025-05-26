# takes the symbols in /symbols and converts them into numbers, and shoves them into symbolData.npy

import cv2 as cv
import os
import numpy as np

symbolNumDict = {}

imgDirectory = os.fsencode("symbols")

for file in os.listdir(imgDirectory):
    filename = "symbols/" + os.fsdecode(file)
    
    symbol = cv.imread(filename, cv.IMREAD_UNCHANGED)
    symbolNum = 0 # using powers of 2 to store 1s and zeros, python can store big ass numbers :)
    
    k = 0
    for j in range(len(symbol)):
        for i in range(len(symbol[j])):
            col = symbol[j][i]
            
            if (col[3] != 0):
                symbolNum += pow(2, k)
            k += 1

    if not symbolNum in symbolNumDict.keys():
        symbolNumDict[symbolNum] = []
    symbolNumDict[symbolNum].append(filename)

np.save("symbolData.npy", symbolNumDict)
