import Tkinter as tk
import tkFileDialog as tfd
import tkMessageBox as tm
import tkFont as tf
import os

win = tk.Tk()
logo = tk.PhotoImage(file = "logo.gif")
img = tk.Label(win, image = logo)
img.grid(row = 0, column = 0)
tnr = tf.Font(family = "Times New Roman", size = 25, weight = "normal")
str = None

def get_name():
	global str
	str = tfd.askopenfilename()
	if str:
		file_entry.grid_forget()
		global display_name
		display_name = tk.Label(win, text = str, font = tnr, relief = "groove")
		display_name.grid(row = 3, column = 0)
		
def check_file():
	global str
	print(str)
	if not str:
		str = file_entry.get()
	if not str:
		tm.showinfo("Error", "Please enter a valid pathname, or browse one!")
		return
	os.system("python checkfile.py " + '\"' + str + '\"')
	file = open("output.txt", "r")
	tm.showinfo("Output", file.read())
	display_name.grid_forget()
	file_entry.grid(row = 3, column = 0)
	
def learning():
	os.system("python trainm.py")
	train_but.grid_forget()
	check_label.grid(row = 1, column = 0)
	browse.grid(row = 2, column = 0)
	file_entry.grid(row = 3, column = 0)
	check_but.grid(row = 4, column = 0)

train_but = tk.Button(win, text = "Train", font = tnr, relief = "groove", command = learning)
train_but.grid(row = 3, column = 0)
check_label = tk.Label(win, text = "Enter File Path Manually Or Browse:", font = tnr, relief = "groove")
browse = tk.Button(win, text = "Browse File", font = tnr, relief = "groove", command = get_name)
display_name = tk.Label(win, text = str, font = tnr, relief = "groove")
file_entry = tk.Entry(win, font = tnr)
check_but = tk.Button(win, text = "Check File For Malware", font = tnr, command = check_file, relief = "groove")
win.mainloop()