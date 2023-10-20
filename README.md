# SGFConverter
Python program to convert sgf files into a text file containing the comma separated moves in alpha numerical format

# Information about program
Contains a gui window allowing you to select your sgf file to convert and save the file as a text document.

You do not have to add an extension to the filename as the program will automatically make it a .txt file.

# How to Use
Can be executed in any command prompt with command
`python3 sgfconvert.py`

Can be converted to a windows executable with the use of the 'pyinstaller' python command with the syntax 
`pyinstaller sgfconvert.py`

If you dont have 'pyinstaller' it can be installed on your windows machine through the command line with the command `pip install -U pyinstaller`

If converted to windows executable it will generate a file and 2 folders 'build' and 'dist'
Located inside the 'dist' folder is a file called 'sgfconvert.exe'

Program can be run by executing this program. The program must be left in this location to work. You can create a shortcut to the program and place that anywhere you want it to be for easy access to execute.
