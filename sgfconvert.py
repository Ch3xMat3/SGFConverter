from tkinter import *
from tkinter import filedialog

def clicked():
	global filename
	filename = filedialog.askopenfilename()

def writeFile():
	global save_file_text
	string = filedialog.asksaveasfilename()
	string = string + '.txt'
	file = open(string,'a+')

	with open(filename, encoding="utf-8") as file2:
		data = file2.read()

	data = data.replace('\n', '')

	nocomment = data.split(';OS')
	data = nocomment[0]
	list = data.split(";")

	file2.close()

	movesequence = []

	for move in list[2:]:
		if move[0] == 'B' or move[0] == 'W':
			coordinate = move[2:4]
			movesequence.append(coordinate.lower())

	finalsequence = []

	for move in movesequence:
		ch1 = move[0]
		if ord(ch1) >= 105:
			ch1 = chr(ord(ch1) + 1)

		finalsequence.append(ch1 + str(20 - (ord(move[1]) - 96)))

	movefinal = ",".join(finalsequence)

	file.write(movefinal)
	file.close()

gui = Tk()
gui.geometry()
gui.title("SGF Converter")

open_file_label = Label(gui, text="open your SGF file here:", font=("Arial", 10), padx=10, pady=10)
open_file_label.grid(column=0, row=0)
open_file_button = Button(gui, text="Select SGF File", command=clicked, padx=10, pady=10)
open_file_button.grid(column=1, row=0)
save_file_label = Label(gui, text="convert and save sgf file:", font=("Arial", 10), padx=10, pady=10)
save_file_label.grid(column=0, row=1)
save_file_button = Button(gui, text="Convert & Save", command=writeFile, padx=10, pady=10)
save_file_button.grid(column=1, row=1)

gui.mainloop()