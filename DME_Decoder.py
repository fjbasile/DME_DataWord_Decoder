hexCodeInput = input("Enter hex value: ")

hexInput = int("0x601878",16)
hexToBinary = bin(hexInput)[5:14]   
count = 0
floatPart = 0.0

for i in bin(hexInput)[13:21]:
  count += 1
  if i == '1':
    floatPart += 2**(-1*count)

print ("The DME Distance is: " + str(int(hexToBinary,2)+floatPart))
