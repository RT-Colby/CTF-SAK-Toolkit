import math
def anythingToDecimal(num,numsystem): # num is number you want to convert (String), numsystem (int) is the current number system of num (1001 could be binary or hex)
    bep = len(str(num))
    print(bep)
    output = 0
    for i in range(0,bep):
        if int(ord(num[i])) > 57: # if it is a char
            letter = int(ord(num[i]))
            if letter > 95: # lower case
                letter -= 87
            else:
                letter -= 55
            output += letter * numsystem ** (len(num) - i - 1)
        else:
            print(int(num[i]) * numsystem ** (len(num) -i - 1))
            output += int(num[i]) * numsystem ** (len(num) -i - 1)
    return output

def decimalToAnything(convert,newsystem):
    bep = math.log(convert,newsystem)
    bep += 1
    bep = int(bep)
    output = ""
    for i in range(0,bep):
        thingy = str(int((convert / newsystem**i) % newsystem))
        convertVar = thingy
        if int(thingy) > 9:
            thingy = int(thingy)
            thingy += 55
            convertVar = str(chr(thingy))
        output = convertVar + output
    return output

#print(decimalToHex(int(input("put in da thinger\t"))))
#print(decimalToAnything(int(input("put in da thinger1\t")),int(input("put in da thinger2\t"))))
#print(anythingToDecimal(input("you know\t"),int(input("the drill\t"))))