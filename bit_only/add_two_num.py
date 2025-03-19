n1 = -5
n2 = -5
MASK = 0xFFFFF

while n2:
    carry = n1 & n2 #gives us right most bit for carry 
    #now after getting the carry we will move it by one place 
    #because 1 bit 1bit => 2bit which is 2^1 meaning it is 10
    n1^=n2
    #this will help in partial addition 
    #as it will add 1011 ^ 1100=> 0111 
    n2=(carry << 1)&MASK
    n1&=MASK

print(n1)



