# SGFConverter
Python program to convert sgf files into a text file containing the comma separated moves in alpha numerical format

# Disclaimer
If sgf is of a game that ended by resignation and also has been reviewed with variations then final text file will contain the moves of the variations after the last move of the game and will have to be manually modified as there is no way to determine when the game ended.

# Information about program
Contains a gui window allowing you to select your sgf file to convert and save the file as a text document.

You do not have to add an extension to the filename as the program will automatically make it a .txt file.

Conversion of the sgf file will drop all lines relating to the players of the game, results of the game, comments added, and any variations played out if the game was reviewed.

Only the main moves of the game will be kept and converted to the comma separated string.

# How to Use
Can be executed in any command prompt with command
`python3 sgfconvert.py`

If running as python program and run into issues with not having python installed or missing libraries then install python from the following link
https://www.python.org/downloads/windows/

Install stable version from matching your system (most likely windows x64)

Can be converted to a windows executable with the use of the 'pyinstaller' python command with the syntax 
`pyinstaller sgfconvert.py`

If you dont have 'pyinstaller' it can be installed on your windows machine through the command line with the command `pip install -U pyinstaller`

If converted to windows executable it will generate a file and 2 folders 'build' and 'dist'
Located inside the 'dist' folder is a file called 'sgfconvert.exe'

Program can be run by executing this program. The program must be left in this location to work. You can create a shortcut to the program and place that anywhere you want it to be for easy access to execute.
