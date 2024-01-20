import cv2 as cv
import os
import numpy as np
import textwrap

symbolDict = np.load('symbolData.npy',allow_pickle='TRUE').item()
symbolSize = 12

framesDirectory = os.fsencode("frames")

for file in os.listdir(framesDirectory):
    filenameReal = os.fsdecode(file)
    filename = "frames/" + filenameReal
    
    frame = cv.imread(filename, cv.IMREAD_UNCHANGED)
    frameString = ""
    
    dimensionY = len(frame)
    dimensionX = len(frame[0])
    dimensionSymbolX = round(dimensionX/symbolSize)
    dimensionSymbolY = round(dimensionY/symbolSize)
    
    for j in range(dimensionY):
        for i in range(dimensionX):
            col = frame[j][i]
            whiteThresh = 127
            
            if (col[3] == 0):
                frameString += "1" #transparent
            elif (col[0] > whiteThresh) and (col[1] > whiteThresh) and (col[2] > whiteThresh):
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
    symbolsGrid = [[cv.imread(symbolsToUse[(dimensionSymbolX * y) + x], cv.IMREAD_UNCHANGED) for x in range(dimensionSymbolX)] for y in range(dimensionSymbolY)]
    #print(symbolsGrid)
    
    rows = []
    for col in range(len(symbolsGrid)):
        rows.append(cv.hconcat(symbolsGrid[col]))
    
    finalFrame = cv.vconcat(rows)
    cv.imwrite("symbolFrames/" + filenameReal, finalFrame)