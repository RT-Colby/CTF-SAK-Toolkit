from tkinter import *
import tkinter.ttk as tkrtk
import sys
import os
from Crypto.JohnPollard import *
from Crypto.CaesarCipher import * 
from Crypto.NumberSystem import *
import webbrowser
from tkinter import messagebox

#test
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
def callback(url):
    webbrowser.open_new(url)
def ccDecryptClick():
		ct = ccEntryCipherText.get()
		output = ""
		if ccEntryKey.get() == "":
			output = bfDecrypt(ct)
			pLabel = Label(ccSheet,text=output)
		else:
			key = int(ccEntryKey.get())
			output=decrypt(ct,key)
			outputLabel = Label(ccSheet, text=output)
			outputLabel.grid(row = 5)
def ccEncryptClick():
	ct = ccEntryCipherText.get()
	key = int(ccEntryKey.get())
	output = encrypt(1,ct,key)
	outputLabel = Label(ccSheet, text=output)
	outputLabel.grid(row = 5)
def testPrint():
	print('It Works!')