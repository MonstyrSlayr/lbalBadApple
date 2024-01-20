import cv2 as cv
import os
import numpy as np
import textwrap
import math

symbolDict = np.load('symbolData.npy',allow_pickle='TRUE').item()
symbolImgs = {}
symbolSize = 12
whiteBG = True

symbolsDirectory = os.fsencode("img")
framesDirectory = os.fsencode("frames")

#load symbols
for file in os.listdir(symbolsDirectory):
    filenameReal = os.fsdecode(file)
    filename = "img/" + filenameReal
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

for file in os.listdir(framesDirectory):
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
            
            # if (col[3] == 0):
            #     frameString += "1" #transparent
            if (col[0] > whiteThresh) and (col[1] > whiteThresh) and (col[2] > whiteThresh):
                frameString += "1" #treat whiteish as transparent
            else:
                frameString += "0" #opaque
    
    #split the frame into groups of symbolSize squares
    daRowsArray = textwrap.wrap(frameString, symbolSize)
    symbolSquares = []
    
    for i in range(dimensionSymbolY):
        for j in range(dimensionSymbolX):
            square = ""
            for x in range(symbolSize):
                indexI = (i * symbolSize * dimensionSymbolX) + (j + (x * dimensionSymbolX))
                square += daRowsArray[indexI]
                
            symbolSquares.append(square)
        
    perfectScore = symbolSize * symbolSize
    symbolsToUse = []
    
    for daSquare in (symbolSquares):
        scoreDict = {}
        symbolToUse = ""
        highScore = 0
        
        for s in symbolDict:
            scoreDict[s] = 0
            
            for c in range(len(symbolDict[s])):
                if (symbolDict[s][c] == daSquare[c]):
                    scoreDict[s] += 1
            
            if (scoreDict[s] == perfectScore):
                symbolToUse = s
                highScore = perfectScore
                break
            elif (scoreDict[s] > highScore):
                highScore = scoreDict[s]
                symbolToUse = s
        symbolsToUse.append(symbolToUse)
        
    #reformat symbolsToUse for concatenation
    symbolsGrid = [[symbolImgs[symbolsToUse[(dimensionSymbolX * y) + x]] for x in range(dimensionSymbolX)] for y in range(dimensionSymbolY)]
    #print(symbolsGrid)
    
    rows = []
    for col in range(len(symbolsGrid)):
        rows.append(cv.hconcat(symbolsGrid[col]))
    
    finalFrame = cv.vconcat(rows)
    newFileName = "symbolFrames/" + filenameReal.replace("jpg", "png")
    cv.imwrite(newFileName, finalFrame)
    print("written " + newFileName)