
alphabetLowerCase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ciphergrid = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
shiftList  = np.array([])
shift = 0
iterate = 0

def decodeCipher(cipherText):
	for letter in alphabetLowerCase:
		for elem in cipherText:
			for number in ciphergrid:
				if letter == elem:
					shiftList[number] = number

decodeCipher('test')
for elm in shift:
	print(elm)

		


