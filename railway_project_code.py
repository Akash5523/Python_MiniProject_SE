from tkinter import *
import os
import sqlite3

def delete2():
  screen3.destroy()

def delete6():
  screen2.destroy()  

def delete7():
  screen1.destroy()  



def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.geometry("500x1000+250+250")
  screen3.title("Registration")
  new_conn = sqlite3.connect('Ticket_Details.db')
  c = new_conn.cursor()
  #Creating a new database 
  # c.execute("""CREATE TABLE Railway_Database(
  #     Name text,
  #     Age integer,
  #     Sex text,
  #     Location text,
  #     Destination text,
  #     Birth_pref text,
  #     Quota text)""")
  def delete8():

  	top.destroy()  

  def submit():

    new_conn = sqlite3.connect('Ticket_Details.db')
    c = new_conn.cursor()

    c.execute("INSERT INTO Railway_Database VALUES(:Name, :Age, :Sex, :Location, :To, :Birth_pref, :Quota, :doj)",
      {
        'Name': name.get(),
        'Age' : age.get(),
        'Sex' : M.get(),
        'Location' : tkvar1.get(),  
        'To' : tkvar2.get(),
        'Birth_pref' : tkvar3.get(),
        'Quota' : tkvar4.get(),
        'doj' : doj.get()


      }) #changed 'destination' ---> 'To' in the above query

    new_conn.commit()
    new_conn.close()
    name.delete(0, END)
    age.delete(0,END)
    M.set('')  #changed here ....no delete attribute..instead used set attribute.
    tkvar1.set('Select Boarding_Station') #changed here ....no delete attribute..instead used set attribute.
    tkvar2.set('Select Destination') #changed here ....no delete attribute..instead used set attribute.
    tkvar3.set('Select Birth') #changed here ....no delete attribute..instead used set attribute.
    tkvar4.set('Select Quota') #changed here ....no delete attribute..instead used set attribute.
    doj.delete(0, END)




  Heading = Label(screen3, text='Passenger Details').grid(row=0,column=1)

  Name = Label(screen3, text='Name').grid(row=1, column='0')
  name =  Entry(screen3, width="25",borderwidth='2')
  name.grid(row='1', column='1',columnspan='10',padx='15',pady='25')

  Age = Label(screen3, text='Age').grid(row=2, column='0')
  age =  Entry(screen3, width="25",borderwidth='2')
  age.grid(row='2', column='1',columnspan='10',padx='15',pady='25')

  M = StringVar()
  Sex = Label(screen3, text='Sex').grid(row=3, column='0')
  Radiobutton(screen3, text="Male", variable=M, value="Male").grid(row=3, column=1)
  Radiobutton(screen3, text="Female", variable=M, value="Female").grid(row=4, column=1)
  Radiobutton(screen3, text="Other", variable=M, value="Other").grid(row=5, column=1)

  Location = Label(screen3, text='From').grid(row=6, column='0')
  # Add a grid
  Location = Frame(screen3)
  Location.grid(column=1,row=6, sticky=(N,W,E,S),pady = 50, padx = 50)
  Location.columnconfigure(0, weight = 1)
  Location.rowconfigure(0, weight = 1)


  # Create a Tkinter variable
  tkvar1 = StringVar(screen3)

  # Dictionary with options
  choices = {'Amravati(AMI)','Badnera Junction(BD)','Mumbai CSMT','Thane(TNA)'}
  tkvar1.set('Select Start Point') # set the default option

  popupMenu = OptionMenu(Location, tkvar1, *choices)
  popupMenu.grid(row = 6, column =1)

  Destination = Label(screen3, text='To').grid(row=7, column='0')
  ## Add a grid
  Destination = Frame(screen3)
  Destination.grid(column=1,row=7, sticky=(N,W,E,S),pady = 50, padx = 50)
  Destination.columnconfigure(0, weight = 1)
  Destination.rowconfigure(0, weight = 1)


  # Create a Tkinter variable
  tkvar2 = StringVar(screen3)

  # Dictionary with options
  choices = {'Amravati(AMI)','Badnera Junction(BD)','Mumbai CSMT','Thane(TNA)'}
  tkvar2.set('Select Destination') # set the default option

  popupMenu = OptionMenu(Destination, tkvar2, *choices)
  #Label(To, text="Choose a Destination").grid(row = 5, column = 1)
  popupMenu.grid(row = 6, column =1)

  Birth_pref = Label(screen3, text='Birth Preference').grid(row=8, column='0')
  # Add a grid
  Birth_pref = Frame(screen3)
  Birth_pref.grid(column=1,row=8, sticky=(N,W,E,S),pady = 50, padx = 50)
  Birth_pref.columnconfigure(0, weight = 1)
  Birth_pref.rowconfigure(0, weight = 1)


  # Create a Tkinter variable
  tkvar3 = StringVar(screen3)

  # Dictionary with options
  choices = {"Select Birth",'Lower','Middle','Upper','Side Lower','Side Upper'}
  tkvar3.set('Select Birth') # set the default option

  popupMenu = OptionMenu(Birth_pref, tkvar3, *choices)
  Label(Location, text="Choose a boarding point").grid(row = 5, column = 1)
  popupMenu.grid(row = 6, column =1)

  Quota = Label(screen3, text='Quota')
  Quota.grid(row=9, column='0')
  # Add a grid
  Quota = Frame(screen3)
  Quota
  Quota.grid(column=1,row=9, sticky=(N,W,E,S),pady = 50, padx = 50)
  Quota.columnconfigure(0, weight = 1)
  Quota.rowconfigure(0, weight = 1)


  # Create a Tkinter variable
  tkvar4 = StringVar(screen3)

  # Dictionary with options
  choices = {"Select Quota",'First Class','Second Class','Genral','Tatkal','Premium Tatkal'}
  tkvar4.set('Select Quota') # set the default option

  popupMenu = OptionMenu(Quota, tkvar4, *choices)
  #Label(From, text="Choose a boarding point").grid(row = 5, column = 1)
  popupMenu.grid(row = 9, column =1)

  DOJ = Label(screen3, text='DOJ').grid(row=10, column='0')
  doj = Entry(screen3, width="25",borderwidth='2')
  doj.grid(row=10,column=1,columnspan='10',padx='15',pady='25')
  #Boarding_Station= Label(root, text='Boarding_Station').grid(row=10, column='0')
  #= Label(root, text='Name').grid(row=0, column='0')

  exit_button = Button(screen3, text="Exit", command=screen3.quit)
  exit_button.grid(row="17", column="0")

  Check_button = Button(screen3, text="Check_Out", command=submit)
  Check_button.grid(row=19,column=1)
 
  top = Toplevel()
  top.title("Preview")
  top.geometry('500x1000+800+300')
  def f1():

    l01 = Label(top, text="Name: ").grid(row=0,column=0)
    Label(top, text=name.get()).grid(row=0,column=1)
    Label(top, text="Age: ").grid(row=1,column=0)
    Label(top, text=age.get()).grid(row=1,column=1)
    Label(top, text="Sex: ").grid(row=2,column=0)
    Label(top, text=M.get()).grid(row=2,column=1)
    Label(top, text="From: ").grid(row=3,column=0)
    Label(top, text=tkvar1.get()).grid(row=3,column=1)
    Label(top, text="To: ").grid(row=4,column=0)
    Label(top, text=tkvar2.get()).grid(row=4,column=1)
    Label(top, text="Birth: ").grid(row=5,column=0)
    Label(top, text=tkvar3.get()).grid(row=5,column=1)
    Label(top, text="Quota: ").grid(row=6,column=0)
    Label(top, text=tkvar4.get()).grid(row=6,column=1)
    Label(top, text="DOJ: ").grid(row=7,column=0)
    Label(top, text=doj.get()).grid(row=7,column=1)
    exit_button = Button(top, text="Confirm", command=delete8)
    exit_button.grid(row="21", column="1", columnspan=2)



  b = Button(screen3, text="Confirm Details", command=f1)
  b.grid(row="15", column="0")
  
def query():
	new_conn = sqlite3.connect('Ticket_Details.db')
	c = new_conn.cursor()

	c.execute('SELECT *, oid FROM Railway_Database')
	records = c.fetchall()
	#print(records)

	print_record = ""
	for record in records:
		print(row[0])
	# 	print_record += str(record)+ "\n"

	# q_label = Label(screen3, text=print_record)
	# q_label.grid(row=50,column=0)

	new_conn.commit()
	new_conn.close()	
	
  
	new_conn.commit()
	new_conn.close()


  

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100+300+300")
  Label(screen4, text = "Password Error").grid()
  Button(screen4, text = "OK", command =delete3).grid()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").grid()
  Button(screen5, text = "OK", command =delete4).grid()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).grid()
  
def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  
  # exit_button = Button(screen2, text="Exit", command=screen2.quit)
  # exit_button.grid(row="15", column="0")


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("5000x500+250+250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").grid()
  Label(screen1, text = "").grid()
  Label(screen1, text = "Username * ").grid()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.grid()
  Label(screen1, text = "Password * ").grid()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.grid()
  Label(screen1, text = "").grid()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).grid()
  exit_button = Button(screen1, text="Exit", command=delete7)
  exit_button.grid(row="15", column="0")

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("5000x500+250+250")
  Label(screen2, text = "Please enter details below to login").grid(row=0,column=2,columnspan=4)
  Label(screen2, text = "").grid(row=1,column=2,columnspan=4)

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").grid(row=2,column=2,columnspan=4)
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.grid(row=3,column=2,columnspan=4)
  Label(screen2, text = "").grid()
  Label(screen2, text = "Password * ").grid(row=5,column=2,columnspan=4)
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.grid(row=6,column=2,columnspan=4)
  Label(screen2, text = "").grid()
  Button(screen2, text = "Login", width = 15, height = 2, command = login_verify).grid(row=8,column=2,columnspan=4)
  Label(screen2, text = "").grid()
  exit_button = Button(screen2, text="Exit", command=delete6)
  exit_button.grid(row="15", column="2",columnspan=4)

  
def main_screen():
  global screen
  screen = Tk()

  screen.geometry('500x500')
  screen.title("IRCTC Login")
  l1 = Label(screen,text = "Welcome to IRCTC Bookings!", bg = "grey", width = "250", height = "3")
  l1.grid(row=0, column=0,columnspan=2, sticky='NESW')
  l2 = Label(screen,text = "")
  l2.grid(row=1, column=0)
  b1 = Button(screen,text = "Login", height = "2", width = "20", command = login)
  b1.grid(row=2, column=0,columnspan=2)
  l3 = Label(screen,text = "")
  l3.grid(row=3, column=0)
  b2 = Button(screen,text = "Register",height = "2", width = "20", command = register)
  b2.grid(row=4, column=0, columnspan=2)
  l4 = Label(screen, text='')
  l4.grid(row=5,column=0)
  b3 = Button(screen, text='Leave Page',command=screen.quit)
  b3.grid(row=6, column=0,columnspan=2)
  screen.mainloop()
  
main_screen()
  