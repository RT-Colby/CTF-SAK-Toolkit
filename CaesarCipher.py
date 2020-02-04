
def encrypt(mode,cipherText,key):
	if mode == 1:
		out = ""
		for letter in cipherText:
			value = ord(letter)
			if value < 65 or value > 122:
				out += " "
			else:
				if value > 96: #if it is lowercase...
					value -= 97
					value += key
					value = value % 26
					value += 97
				else:
					value -= 65
					value += key
					value %= 26
					value += 65
				out += chr(value)
	print(out)

def bfDecrypt(ciphertext):
	dictionary = ["the","be","to","of","and","a","in","that","have","I","it","for","not","on","with","as","you","do","flag","at","this","over","would","there","will","he","she","person","than","then","you","your","what","is"]
	outs = []
	for i in range(0,26):
		out = ""
		for letter in ciphertext:
			value = ord(letter)
			if value < 65 or value > 122:
				out += " "
			else:
				if value > 96: #if it is lowercase...
					value -= 97
					value -= i
					value += 26
					value = value % 26
					value += 97
				else:
					value -= 65
					value -= i
					value += 26
					value %= 26
					value += 65
					out += chr(value)
					outs.append([out,0])
					print(out + "\tkey of " + str(i))
	print()
	print("############################")
	print("#     PROBABILITY MAP      #")
	print("############################")
	for bep in outs:
		for word in bep[0].split(" "):
			for probword in dictionary:
				if word == probword:
					bep[1] += 1
	maximum = 0
	for bep in outs:
		if bep[1] > maximum:
			maximum = bep[1]
	for i in range(0, maximum + 1):
		for bep in outs:
			if bep[1] == maximum - i:
				print(bep[0] + "\t prob of: " + str(maximum - i) + " vs " + str(maximum))
        #print()

def decrypt(mode,cipherText,key):
    #shift = int(input("loop?"))
	out = ""
	for letter in cipherText:
		value = ord(letter)
		if value < 65 or value > 122:
			out += " "
		else:
			if value > 96: #if it is lowercase...
					value -= 97
					value -= key
					value += 26
					value = value % 26
					value += 97
			else:
				value -= 65
				value -= key
				value += 26
				value %= 26
				value += 65
			out += chr(value)
	print(out)
   