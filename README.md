<h1>
Luck be a Landlord: Silhouette to Symbols Converter
</h1>

[![Bad Apple but it's Luck Be a Landlord](https://i9.ytimg.com/vi_webp/f5CtDEwnOLw/maxresdefault.webp?v=68358012&sqp=CIyN18EG&rs=AOn4CLCyAu-5WmyURFn5feJFw9RfmrNrJQ)](https://youtu.be/f5CtDEwnOLw)
[Bad Apple but it's Luck Be a Landlord](https://youtu.be/f5CtDEwnOLw)

a tool that takes frames and LbaL-ifies them. feel free to make your own images and videos with this tool, and even use modded symbols

delete the empty.txt files before use please

<h2>
Folders:
</h2>

- <b>/frames</b> - this is where the original silhouettes go
- <b>/symbols</b> - this is where the symbol images go
- <b>/symbolFrames</b> - this is the output file, containing the silhouettes made from symbols

<h2>
Files and their purposes:
</h2>

- <b>videoToFrames.py</b> - takes a video and outputs frames into /frames
- <b>symbolsToPixels.py</b> - takes the symbols in /symbols, converts them into strings of 1s and 0s to symbolData.npy depending on their opacity makeup
- <b>framesToSymbols.py</b> - converts the files in /frames to symbol frames in /symbolFrames
- <b>symbolFramesToVideo.py</b> - takes the symbol frames in /symbolFrames and outputs a video

<h2>
Required packages:
</h2>

- opencv
- numpy
- textwrap
- os
- csv

any version should be fine :)