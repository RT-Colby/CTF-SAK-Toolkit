alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ciphergrid = []
cipher = raw_input()
shift = 0
iterate = 0

for elem in cipher:
	ciphergrid[1] = elem
	iterate = iterate + 1

for x in ciphergrid:
	print(x)
