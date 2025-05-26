<h1>
Luck Be a Landlord: Silhouette to Symbols converter
</h1>

<h2>
Folders:
</h2>

- <b>/frames</b> - this is where the original silhouettes go
- <b>/img</b> - this is where the symbol images go
- <b>/symbolFrames</b> - this is the output file, containing the silhouettes made from symbols

<h2>
Files and their purposes:
</h2>

- <b>framesToSymbols.py</b>
- <b>symbolFramesToVideo.py</b>
- <b>symbolsToPixels.py</b> - takes the symbols in /img, converts them into strings of 1s and 0s depending on their
- <b>videoToFrames.py</b> - converts a video into frames

<h2>
Required packages:
</h2>

- opencv
- numpy
- textwrap
- os