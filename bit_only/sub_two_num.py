a = 12
b = -4
MASK = 0XFFFFF
while b != 0:
    carry = a&b
    a^=b
    b = carry<<1
    a&=MASK

print(a)
