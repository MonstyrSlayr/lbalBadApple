<h1>
Luck Be a Landlord: Silhouette to Symbols Converter
</h1>

[![Bad Apple but it's Luck Be a Landlord](https://i9.ytimg.com/vi_webp/Rx8IFNVVKEI/maxresdefault.webp?v=65ad71e4&sqp=COj-zsEG&rs=AOn4CLDPuWSs9yJ7dH6jWJb11TV9NZVm8Q)](https://www.youtube.com/watch?v=Rx8IFNVVKEI)

a tool that takes frames and LBaL-ifies them. feel free to make your own images and videos with this tool, and even use modded symbols

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

any version should be fine :)