# it's hard to believe but this file actually converts frames to symbols
# takes every symbol (already converted into a string)
# takes every frame, slices it up into symbol sized squares, and converts it into a string
# compare it with symbols and takes the best fit
# make a new frame made of just symbols
# profit

import random
import time
import cv2 as cv
import os
import numpy as np
import textwrap
import math
from csvWriting import write_csv_row, count_strings

symbolNumDict = np.load('symbolData.npy',allow_pickle='TRUE').item() # RUN SYMBOLS TO PIXELS FIRST
symbolImgs = {}
symbolSize = 12 # symbols are 12 by 12 pixels, hard coded
whiteBG = True # false for transparent background
frameLowerLimit = 0 # for debugging, set to 0 to unlimit
frameUpperLimit = 100 # for debugging, set to 0 to unlimit
writeDataToFile = True # set to false to omit data

symbolsDirectory = os.fsencode("symbols")
framesDirectory = os.fsencode("frames")

# load all symbols into memory (is this a good idea? probably not)
previousFrameSymbols = []
for file in os.listdir(symbolsDirectory):
    filenameReal = os.fsdecode(file)
    filename = "symbols/" + filenameReal
    daImage = cv.imread(filename, cv.IMREAD_UNCHANGED)
    if whiteBG:
        for i in range(len(daImage)):
            for j in range(len(daImage[i])):
                if (daImage[i][j][3] == 0):
                    daImage[i][j][0] = 255
                    daImage[i][j][1] = 255
                    daImage[i][j][2] = 255
                    daImage[i][j][3] = 255
    symbolImgs[filename] = daImage

# parse every frame
frameCount = 0
startTimeReal = time.time()
for file in os.listdir(framesDirectory):
    if (frameLowerLimit != 0) and (frameCount < frameLowerLimit):
        frameCount += 1
        continue

    startTime = time.time()
    
    filenameReal = os.fsdecode(file)
    filename = "frames/" + filenameReal
    
    frame = cv.imread(filename, cv.IMREAD_UNCHANGED)
    frameString = ""
    
    dimensionY = len(frame)
    dimensionX = len(frame[0])
    dimensionSymbolX = math.floor(dimensionX/symbolSize)
    dimensionSymbolY = math.floor(dimensionY/symbolSize)
    
    for j in range(dimensionY):
        for i in range(dimensionX):
            col = frame[j][i]
            whiteThresh = 127
            
            if (col[0] > whiteThresh) and (col[1] > whiteThresh) and (col[2] > whiteThresh):
                frameString += "0" # treat whiteish as transparent
            else:
                frameString += "1" # opaque
    
    # split the frame into groups of symbolSize squares
    daRowsArray = textwrap.wrap(frameString, symbolSize)
    symbolSquares = []
    
    # make symbolsquare strings into nums for each
    for i in range(dimensionSymbolY):
        for j in range(dimensionSymbolX):
            squareNum = 0
            k = 0

            for x in range(symbolSize):
                indexI = (i * symbolSize * dimensionSymbolX) + (j + (x * dimensionSymbolX))
                for char in daRowsArray[indexI]:
                    if (char == "1"):
                        squareNum += pow(2, k)
                    k += 1
                
            symbolSquares.append(squareNum)
        
    perfectScore = symbolSize * symbolSize
    symbolsToUse = []
    
    # give every square a symbol
    # compares symbolsquare to a symbolData key and takes the best match
    # then takes a random symbol from the key
    for i in range(len(symbolSquares)):
        daSquareNum = symbolSquares[i]
        scoreDict = {}
        symbolNumToUse = 0
        highScore = 0
        
        for bigNum in symbolNumDict:
            scoreDict[bigNum] = 0
            
            for n in range(perfectScore):
                if ((bigNum & (1 << n)) == (daSquareNum & (1 << n))): # dark magic
                    scoreDict[bigNum] += 1
            
            if (scoreDict[bigNum] > highScore):
                highScore = scoreDict[bigNum]
                symbolNumToUse = bigNum

        symbolToUse = None
        if ((len(previousFrameSymbols) > i) and (previousFrameSymbols[i] in symbolNumDict[symbolNumToUse])):
            symbolToUse = previousFrameSymbols[i]
        else:
            symbolToUse = random.choice(symbolNumDict[symbolNumToUse])
        symbolsToUse.append(symbolToUse)
    
    previousFrameSymbols = symbolsToUse
    if writeDataToFile:
        symbolsToUseCopy = [symbol.replace("symbols/", "").replace(".png", "") for symbol in symbolsToUse]
        daData = count_strings(symbolsToUseCopy)
        write_csv_row("symbolExportData.csv", filenameReal.replace(".jpg", ""), daData)

    # reformat symbolsToUse for concatenation
    symbolsGrid = [[symbolImgs[symbolsToUse[(dimensionSymbolX * y) + x]] for x in range(dimensionSymbolX)] for y in range(dimensionSymbolY)]
    
    rows = []
    for col in range(len(symbolsGrid)):
        rows.append(cv.hconcat(symbolsGrid[col]))
    
    # export to symbolframes
    finalFrame = cv.vconcat(rows)
    newFileName = "symbolFrames/" + filenameReal.replace("jpg", "png")
    cv.imwrite(newFileName, finalFrame)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"written {newFileName} in {elapsedTime:.4f} seconds")

    frameCount += 1
    if (frameUpperLimit != 0) and (frameCount >= frameUpperLimit):
        break

endTimeReal = time.time()
elapsedTimeReal = endTimeReal - startTimeReal
print(f"finished writing in {elapsedTimeReal:.4f} seconds")
