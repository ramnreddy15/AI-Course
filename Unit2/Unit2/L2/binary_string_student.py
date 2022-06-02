import math
"""   
    +--------- PYTHON BIT OPERATORS, FUNCTIONS, AND TRICKS ----------------+
    |  operator          meaning                  examples                 |
    |   &          and                     1010 & 1100 = 1000              |
    |   |          non-exclusive or        1010 | 1100 = 1110              |
    |   ^          exclusive or            1010 ^ 1100 = 0100              |
    |   ~          not (flip all bits)    ~1010        = ????              |
    |              flip all bits           0x1F-(0b11010) = 101            |
    |   <<         shift left  n bits      101    << 3 = 101000            |
    |   >>         shift right n bits      101000 >> 3 = 101               |
    +----------------------------------------------------------------------+
    |   0b or 0B   interpret as binary      0b10101    = 21                |
    |   bin()      express as binary        bin(21)    = 10101             |
    +----------------------------------------------------------------------+
    |  turn ON  nth bit from right: num |=  (1 << n)                       |
    |  turn OFF nth bit from right: num &= ~(1 << n)                       |
    |  flip     nth bit from right: num ^=  (1 << n)                       |
    |  test     nth bit from right: if (num & (1 << n))  > 0: ...          |
    |                               if (num & (1 << n)) == 0: ...          |
    |  clear the right-most bit:    num = num & (num-1)                    |
    |  smear right-most 1 to right: num | (num-1)                          |
    |  extract right-most 1:        num = num & -num (e.g., 101100 ->10)   |
    |  extract nth bit from left:   bit = (num >> n) & 1                   |
    |  mod 2**n:                    x mod 2**n = x &(2**n - 1)             |
    +----------------------------------------------------------------------+
    |  Below, the 0 is a zero, not a letter in 0b (= 0B).                  |
    |  print (0b10101)           # = 21                                    |
    |  print ( int("10101", 2) ) # = 21 (string to binary integer)         |
    |  print(bin(21))            # = 0b10101                               |
    |  print(bin(21)[2:])        # =   10101                               |
    |  n = 0b1001                                                          |
    |  print(n.bit_length())     # = 4                                     |
    +----------------------------------------------------------------------+
"""

# Question 1: What is the 4-bit binary representation of number?
def fourBitBinaryRep(number):
    if str(number)[0] == "-":
        return (bin(number+(2**32)))[-4:]
    else:
        return bin(number)[2:]

# Question 2: # Create a binary number of max bits. Initially set every bit to 1. By the sieve method
# of Eratosthenes, set to zero any bit whose position number is not a prime number.

def sieveOfEratosthenesUsingBits(max):     # max = the number of bits
    num = int("1"*100, 2)
    for i in range(2,int(math.sqrt(max))+1):
        if (bin(num) & (1 << i))%2 == 0:
            j = 2
            while(j*i <= max):
                num &= ~(1<<j*i)
                j+=1      
    num = bin(num)
    print(num)
    for i,j in enumerate(list(str(num))):
        if j == "1":
            print(i+1, end=" ")
    #    tempBits = "0"+"1"*max
#    maxBin = "0b"
#    tempBits = list(tempBits)
#    tempBits[1] = "0"
#    for i in range(2,int(max/2)+1):
#         if (tempBits[i]) == "1":
#             j = 2
#             while(j*i <= max):
#                 tempBits[j*i] = "0"
#                 j+=1       
#    tempBits = "".join(tempBits)            
#    maxBin = maxBin+tempBits[::-1][:-1]
#    for i,j in enumerate(maxBin[::-1]):
#         if j == "1":
#             print(i+1, end=" ")
#    print()
 
  
def main():
   number = -13    
   print(fourBitBinaryRep(number))  # -13 (= -0b1101) is 0011
   sieveOfEratosthenesUsingBits(100)   # total 25 prime numbers should be printed
   
if __name__ == '__main__':  main()

# print(bin(5)[2:])
# n = 0b1001
# print(n)
# print(bin(n)[2:])
# print(n.bit_length())
# print(int('101', 2))

# # operators
# a = 0b1001 # 1001
# b = 0b1100

# print ('and', bin(a & b)[2:])  # 1000

# print ('or', bin(a | b)[2:])  # 1101

# print ('xor', bin(a * b)[2:])  # 101

# print ('not', ~a) # signed bit number -10

# print ('shift left', bin(a << 1)[2:], a<<1) # 10010 18
# print ('shift right', bin(a >> 1)[2:], a>>1) # 100 4

# # useful skills

# num = 0b1000

# n=3

# num |= (1 << (n-1))
# print (bin(num)[2:])

# num & ~(1 << (n-1))
# print (bin(num)[2:])

# turn ON 3rd bit from right
# 1100

# turn OFF 3rd bit from right
# 1000