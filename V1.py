import time
import sys
from JohnPollard import *



print('Hello Welcome to the CTF Swiss Army Knife Toolkit! ')
print('Created by Colby Frey\n')
time.sleep(1)
print('Please select your desired tool \n')


def selectionScreen():
	print('1. John Pollard n-1')
	print('2. Rot-13')
	print('3. Exit')

	tool = raw_input()

	if tool == '1':
		number = input('Please enter a number\n')
		print(pollard_P_1(number))
		sys.exit(0)
	if tool == '2':
		print('not done yet')
	if tool == '3':
		sys.exit(0)

	else:
		print('Invalid Selection, Try again')
		selectionScreen()




selectionScreen()