#Imports files to build GUI
from WindowJohnPollard import *
from AccessMethods import *

#Imports crypto files and scripts
from Crypto.JohnPollard import *
from Crypto.CaesarCipher import * 
from Crypto.NumberSystem import *

class MyTkWindow:
	def __init__(self):

		#Create window
		self.master = Tk()
		self.root.master.title('CTF SAK Toolkit')
		self.master.geometry('500x300')
		selfl.root.master.iconbitmap(r'assets\blue-SAK.ico')


		#Notebook

		self.menuNB = tkrtk.Notebook(master)
		self.touSheet = tkrtk.Frame(menuNB)
		self.rsaSheet = tkrtk.Frame(menuNB)
		self.ccSheet = tkrtk.Frame(menuNB)
		self.menuNB.add(touSheet, text = "Terms of Use")
		self.menuNB.add(rsaSheet, text = "John Pollard", state='hidden')
		self.menuNB.add(ccSheet, text = "Caesar Cipher", state='hidden')
		self.menuNB.grid(row = 0)

		#TOU Windoow
		self.welcome_label = Label(touSheet, text='Welcome to the CTF Swiss Army Knife Toolkit!\n Created by Colby Frey\n', font=('Rouge', 14)) 
		self.help_label = Label(touSheet, text='special thanks to Jackson Elsmore for helping contribute to the project')
		self.termsOfUseLabel = Label(touSheet, text='By clicking the "I agree" button you agree to not pull an Austin ', font=('Rouge',11))
		self.touLinkLabel = Label(touSheet, text='Link to README', font=('Rouge', 11), fg='blue')
		self.agreeButton = Button(touSheet, text='I agree', font=('Rouge', 9), command=agreeClick,padx=100, pady=5, bd=3)


		#TOU Grid
		self.welcome_label.grid(row=1, column=0, padx=25, pady=25)
		self.help_label.grid(row = 2 )
		self.termsOfUseLabel.grid(row=2, column=0, padx=25)
		self.touLinkLabel.grid()
		self.agreeButton.grid()
		self.touLinkLabel.bind("<Button-1>", lambda e: callback("https://github.com/RT-Colby/CTF-SAK-Toolkit/blob/master/README.md"))

	def start(self):
		self.root.mainloop() #start monitoring and updating the GUI





