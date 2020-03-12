
def encrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e
def decrypt(text):
	counter = 0
	game = []
	numberText = 0
	while counter < 26: 
		for letter in text:
			numberText += (ord(letter)-counter)
		
		game.append(plaintext)
		counter +=1
	for item in game:
		print(item)

decrypt(':<M?TLH8<A:KFBG@V')



#assert encrypt(flag, shift) == ':<M?TLH8<A:KFBG@V'