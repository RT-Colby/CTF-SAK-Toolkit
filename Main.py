from tkinter import *
import sys
import os
from JohnPollard import *

#Create window
master = Tk()
master.title('CTF SAK-Toolkit')
master.geometry('500x300')

#button method
def buttonClick():
	text = pollard_P_1(int(jpEntry.get()))
	pLabel = Label(master, text=text)
	pLabel.grid(row = 5)




#Intro labels
welcome_label = Label(master, text='Welcome to the CTF Swiss Army Knife Toolkit!\n Created by Colby Frey test', font=('Rouge', 14))

termsOfUseLabel = Label(master, text='By clicking the "I agree" button you agree to the terms of use', font=('Rouge',8))

#Entries
jpEntry = Entry(master, borderwidth=2)

#Buttons
agreeButon = Button(master, text='Run JohnPollard!', command=buttonClick)

#Grid Assignments
welcome_label.grid(row = 1, column=0)
termsOfUseLabel.grid(row=2, column=0)
agreeButon.grid(row=4)
jpEntry.grid(row=3)

#Part
part_text = StringVar()





master.mainloop()
