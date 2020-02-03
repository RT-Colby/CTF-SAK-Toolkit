from tkinter import *
import tkinter.ttk as tkrtk
import sys
import os
from JohnPollard import *

#Initalize intial values
labelsList = []
buttonsList = []
entriesList = []


#Create window
master = Tk()
master.title('CTF SAK-Toolkit')
master.geometry('500x300')


#Methods
def buttonClick():
	text = pollard_P_1(int(jpEntry.get()))
	pLabel = Label(master, text=text)
	pLabel.grid(row = 5)
def restWindow():
	for label in labelsList:
		labelsList.destory()
	for button in buttonsList:
		buttonsList.destory()
	for Entry in entriesList:
		entriesList.destory()


#Intro labels
welcome_label = Label(master, text='Welcome to the CTF Swiss Army Knife Toolkit!\n Created by Colby Frey test', font=('Rouge', 14)) 
termsOfUseLabel = Label(master, text='By clicking the "I agree" button you agree to the terms of use', font=('Rouge',8))
testNB = tkrtk.Notebook(master)
touSheet = tkrtk.Frame(testNB)
testNB.add(touSheets, text = "tou")

#Entries
jpEntry = Entry(master, borderwidth=2)

#Buttons
agreeButton = Button(master, text='Run JohnPollard!', command=buttonClick)

#Grid Assignments
welcome_label.grid(row = 1, column=0)
termsOfUseLabel.grid(row=2, column=0)
agreeButton.grid(row=4)
jpEntry.grid(row=3)
testNB.grid()

#List assignments
labelsList.append(welcome_label)
labelsList.append(termsOfUseLabel)
buttonsList.append(agreeButton)
entriesList.append(jpEntry)


#Part
part_text = StringVar()





master.mainloop()
