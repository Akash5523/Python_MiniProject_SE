# to create a working calculator 

from tkinter import *


root = Tk()

root.title("CALCULATOR")# to change title


entery =  Entry(root, width="25",borderwidth='5')
entery.grid(row='0', column='0',columnspan='3',padx='15',pady='25')

def onclick(n):
	entery.insert(n+1, n)
	#entery.delete()
	return

def on_clear():
	entery.delete(0, END)

def on_add():
	n1 = entery.get()
	global num_n1
	global operation
	operation = 'add'
	num_n1 = int(n1)
	entery.delete(0, END)

def on_sub():
	n1 = entery.get()
	global num_n1
	global operation
	operation = 'subtract'
	num_n1 = int(n1)
	entery.delete(0, END)

def on_mul():
	n1 = entery.get()
	global num_n1
	global operation
	operation = 'multiply'
	num_n1 = int(n1)
	entery.delete(0, END)

def on_div():
	n1 = entery.get()
	global num_n1
	global operation
	operation = 'divide'
	num_n1 = int(n1)
	entery.delete(0, END)

def on_equal():
	n2 = entery.get()
	entery.delete(0, END)
	if operation == 'add':
		entery.insert(0, num_n1+int(n2))

	if operation == 'subtract':
		entery.insert(0, num_n1-int(n2))
	
	if operation == 'multiply':
		entery.insert(0, num_n1*int(n2))
	
	if operation == 'divide':
		entery.insert(0, num_n1/int(n2))

button0 	= Button(root, text = '0', command=lambda:onclick(0), padx="28", pady="12")
button1 	= Button(root, text = '1', command=lambda:onclick(1), padx="28", pady="12")
button2 	= Button(root, text = '2', command=lambda:onclick(2), padx="28", pady="12")
button3 	= Button(root, text = '3', command=lambda:onclick(3), padx="28", pady="12")
button4 	= Button(root, text = '4', command=lambda:onclick(4), padx="28", pady="12")
button5 	= Button(root, text = '5', command=lambda:onclick(5), padx="28", pady="12")
button6 	= Button(root, text = '6', command=lambda:onclick(6), padx="28", pady="12")
button7 	= Button(root, text = '7', command=lambda:onclick(7), padx="28", pady="12")
button8 	= Button(root, text = '8', command=lambda:onclick(8), padx="28", pady="12")
button9     = Button(root, text = '9', command=lambda:onclick(9), padx="28", pady="12")
button_add  = Button(root, text = '+', command=on_add, padx="26.15", pady="12")
button_sub 	= Button(root, text = '-', command=on_sub, padx="29", pady="12")
button_mul 	= Button(root, text = '*', command=on_mul, padx="28", pady="12")
button_div	= Button(root, text = '/', command=on_div, padx="30", pady="12")
button_ans  = Button(root, text = '=', command=on_equal, padx="26", pady="12")
clear  = Button(root, text = 'CLEAR', command=lambda:on_clear(), padx="91", pady="12")

button0.grid(row='5', column='0')
button1.grid(row='4', column='0')
button2.grid(row='4', column='1')
button3.grid(row='4', column='2')
button4.grid(row='3', column='0')
button5.grid(row='3', column='1')
button6.grid(row='3', column='2')
button7.grid(row='2', column='0')
button8.grid(row='2', column='1')
button9.grid(row='2', column='2')
button_ans.grid(row='6', column='0')
button_div.grid(row='6', column='1')
button_mul.grid(row='6', column='2')
button_sub.grid(row='5', column='2')
button_add.grid(row='5', column='1')
clear.grid(row='7',column='0',columnspan='3')

root.mainloop()
