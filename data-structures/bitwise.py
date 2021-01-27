#complement(~)
#~1=0
#~0=1

#00001100 -> 11110011
#Two's complement
#find number in binary then reverse the number and add 1 in binary
print(~12)
print(~-13)
print(~4)
print(~-5)

#12 in binary = 00001100
#12 in binary = 00001101

print(12&13) #00001100
print(12|13) #00001101
print(25&30) #0001100

#XOR
print(12^13) #00000001

#left shift
print(10 << 2) #1010.0000 -> 101000.