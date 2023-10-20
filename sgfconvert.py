# tkinter library used to provide gui display for program
from tkinter import *
from tkinter import filedialog

# Get name of sgf file and store in global variable
def clicked():
	global filename
	filename = filedialog.askopenfilename()

# Create and write to new file reading from sgf file
def writeFile():
	# Get the name of new file to create
	global save_file_text
	string = filedialog.asksaveasfilename()

	# make the file a .txt file and open it
	string = string + '.txt'
	file = open(string,'a+')

	# read from sgf file
	with open(filename, encoding="utf-8") as file2:
		data = file2.read()

	# remove all new lines make one long string
	data = data.replace('\n', '')

	# remove all lines after the official game (ie variations)
	nocomment = data.split(';OS')

	# grab only the game moves
	data = nocomment[0]

	# split on semicolon to put each game move in its own cell of an array
	list = data.split(";")

	movesequence = []

	# loop through all moves (ignore first 2 items as they are information about players and results)
	for move in list[2:]:
		# Double check cell contains a move by starting with a B or W
		if move[0] == 'B' or move[0] == 'W':
			# grab move coordinates and add to list
			coordinate = move[2:4]
			movesequence.append(coordinate.lower())

	finalsequence = []

	# loop through all game moves
	for move in movesequence:
		ch1 = move[0]

		# if letter is 'i' or higher then move up 1 as go boards dont have an 'i' column
		if ord(ch1) >= 105:
			ch1 = chr(ord(ch1) + 1)

		# add new coordinates to final list converting second letter then number
		# numbers on a go board count from bottom to top so reverse the number by subtracting it from 20
		finalsequence.append(ch1 + str(20 - (ord(move[1]) - 96)))

	# join list into a comma separated string
	movefinal = ",".join(finalsequence)

	# write string to new file and close it
	file.write(movefinal)
	file.close()

# create gui window for user
gui = Tk()
gui.geometry()
gui.title("SGF Converter")

# create label and button to select sgf file
open_file_label = Label(gui, text="open your SGF file here:", font=("Arial", 10), padx=10, pady=10)
open_file_label.grid(column=0, row=0)
open_file_button = Button(gui, text="Select SGF File", command=clicked, padx=10, pady=10)
open_file_button.grid(column=1, row=0)

# create label and button to select location and name of file to create
save_file_label = Label(gui, text="convert and save sgf file:", font=("Arial", 10), padx=10, pady=10)
save_file_label.grid(column=0, row=1)
save_file_button = Button(gui, text="Convert & Save", command=writeFile, padx=10, pady=10)
save_file_button.grid(column=1, row=1)

# create mainloop of gui to keep open upon program execution
gui.mainloop()