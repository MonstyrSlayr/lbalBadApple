import cv2 as cv
import os

symbolFramesDirectory = os.fsencode("symbolFrames")
symbolFramesCount = sum(1 for _, _, files in os.walk("symbolFrames") for f in files)
frames = [None] * symbolFramesCount

for file in os.listdir(symbolFramesDirectory):
    filenameReal = os.fsdecode(file)
    filename = "symbolFrames/" + filenameReal
    
    frame = cv.imread(filename, cv.IMREAD_UNCHANGED)
    daIndex = int(filenameReal.replace(".png", "").replace("frame", ""))
    frames[daIndex] = frame

print(len(frames))

w = 480
h = 360

writer = cv.VideoWriter("videoOutput.mp4", -1, 30.0, (w, h))

for frame in frames:
    writer.write(frame)

writer.release()