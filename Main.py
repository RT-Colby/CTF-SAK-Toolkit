from tkinter import *
import tkinter.ttk as tkrtk
import sys
import os
import webbrowser
from tkinter import messagebox

#Imports crypto files and scripts
from Crypto.JohnPollard import *
from Crypto.CaesarCipher import * 
from Crypto.NumberSystem import *

	
#Initalize intial values
sheetList = []

#Create window
master = Tk()
master.title('CTF SAK Toolkit')
master.geometry('500x300')
master.iconbitmap(r'assets\blue-SAK.ico')


#Methods

def jpButonClick():
	if jpEntry.get() == '':
		messagebox.showerror('Required Field', 'Please enter the number for n')
	else:
		text = pollard_P_1(int(jpEntry.get()))
		pLabel = Label(rsaSheet, text=text)
		pLabel.grid(row = 5)

def restWindow():
	for label in labelsList:
		labelsList.destory()
	for button in buttonsList:
		buttonsList.destory()
	for Entry in entriesList:
		entriesList.destory()
def agreeClick():
	agreeWindow = Tk()
	agreeWindow.title('CTF SAK Toolkit')
	agreeWindow.geometry('500x100')
	agreeWindow.iconbitmap(r'assets\blue-SAK.ico')
	agreedLabel=Label(agreeWindow, text='Thank you for agreeing to the terms of use, you may now use the program freely. \n You may now close this window', font=('Rouge', 10))
	agreedLabel.pack()
	menuNB.tab(rsaSheet,state='normal')
	menuNB.tab(ccSheet,state='normal')
	menuNB.tab(nsSheet,state='normal')
def callback(url):
    webbrowser.open_new(url)
def ccDecryptClick():
		ct = ccEntryCipherText.get()
		output = ""
		counter = 0
		if ccEntryKey.get() == '' :
			output = bfDecrypt(ct)
			#CC Brute Force List
			bfList = Listbox(ccSheet)
			for x in output:
				bfList.insert(counter, x)
				counter += 1
			bfList.grid(row=5,column=1)
		elif ccEntryKey.get().isalpha():
			messagebox.showerror('Required Field', 'Please enter a valid decryption key')
		else:
			try:
				key = int(ccEntryKey.get())
			except:
				messagebox.showerror('Required Field', 'Please enter a valid encryption key')
				return
			output=decrypt(ct,key)
			ccEntryCipherText.delete(0, END)
			ccEntryCipherText.insert(0, output)
			outputLabel = Label(ccSheet, text=output, state='active')
			resultsLabel = Label(ccSheet, text='Output from decrypt= ')
			resultsLabel.grid(row= 4, column =2)
			outputLabel.grid(row = 4, column = 3)

def ccEncryptClick():
	if ccEntryKey.get() == '' or ccEntryKey.get().isalpha():
		messagebox.showerror('Required Field', 'Please enter a valid encryption key')
	else:
		try:
			key = int(ccEntryKey.get())
		except:
			messagebox.showerror('Required Field', 'Please enter a valid encryption key')
			return
		ct = ccEntryCipherText.get()
		output = encrypt(1,ct,key)
		ccEntryCipherText.delete(0, END)
		ccEntryCipherText.insert(0, output)
		outputLabel = Label(ccSheet, text=output)
		resultsLabel = Label(ccSheet, text='Output from encrypt')
		resultsLabel.grid(row= 4, column =2)
		outputLabel.grid(row = 4, column = 3)


#Notebook
menuNB = tkrtk.Notebook(master)
touSheet = tkrtk.Frame(menuNB)
rsaSheet = tkrtk.Frame(menuNB)
ccSheet = tkrtk.Frame(menuNB)
nsSheet = tkrtk.Frame(menuNB)

menuNB.add(touSheet, text = "Terms of Use")
menuNB.add(rsaSheet, text = "RSA Attacks", state='hidden')
menuNB.add(ccSheet, text = "Caesar Ciphers", state='hidden')
menuNB.add(nsSheet, text = "Number Systems", state='hidden')
menuNB.grid(row = 0)


#TOU Windoow
welcome_label = Label(touSheet, text='Welcome to the CTF Swiss Army Knife Toolkit!\n Created by Colby Frey\n', font=('Rouge', 14)) 
help_label = Label(touSheet, text='special thanks to Jackson Elsmore for helping contribute to the project')
termsOfUseLabel = Label(touSheet, text='By clicking the "I agree" button you agree to not pull an Austin ', font=('Rouge',11))
touLinkLabel = Label(touSheet, text='Link to README', font=('Rouge', 11), fg='blue')
agreeButton = Button(touSheet, text='I agree', font=('Rouge', 9), command=agreeClick,padx=100, pady=5, bd=3)

#TOU Grid
welcome_label.grid(row=1, column=0, padx=25, pady=25)
help_label.grid(row = 2 )
termsOfUseLabel.grid(row=2, column=0, padx=25)
touLinkLabel.grid()
agreeButton.grid()
touLinkLabel.bind("<Button-1>", lambda e: callback("https://github.com/RT-Colby/CTF-SAK-Toolkit/blob/master/README.md"))

#RSA Window
jpUsageLabel = Label(rsaSheet, text='John Pollard p-1 attack')
jpEntry = Entry(rsaSheet, borderwidth=2)
runJP = Button(rsaSheet, text='Run JohnPollard!', command=jpButonClick)
rsaLabel = Label(rsaSheet, text='')

#JPGrid
jpUsageLabel.grid()
jpEntry.grid(row=1)
runJP.grid(row=2, padx=20, pady=20)

#Ceaser Cipher Window
ccUsageLabel = Label(ccSheet, text='Enter the text and the key below')
ccTextLabel = Label(ccSheet, text='Cipher Text')
ccKeyLabel = Label(ccSheet, text='Rotation Key')
ccEntryCipherText = Entry(ccSheet, borderwidth=2)
ccEntryKey = Entry(ccSheet, borderwidth=2)
runDecrypt = Button(ccSheet, text='Decrypt', command=ccDecryptClick)
runEncrypt = Button(ccSheet, text='Encrypt', command=ccEncryptClick)

#CCGrid
ccUsageLabel.grid(column=1)
ccTextLabel.grid(row=2,column=0)
ccEntryCipherText.grid(row=2, column=1)
ccKeyLabel.grid(row=3,column=0)
ccEntryKey.grid(row=3,column=1)
runDecrypt.grid(row=4,column=1)
runEncrypt.grid(row=4, column=0)



#Loop
master.mainloop()
