'''
to check if a value is odd meaning is not divisible by 2 is an odd value
so in bits we only have power of 2
meaning if a bit has to be odd it must have a 2^0 as bit at the right most place
so we can check for the presence of that bit their.
to know if it is odd or even

'''
print('odd')
a = 3
a&=1
print(a)
print()
print("************************************************************")
print(
'''
we will use & and bitwise operator to do this in opposite will be 1

so how it works is  0 & 1  = 0, only 1 & 1 = 1
now

any value would be like this
100101 when we & bitwise operation on this it will give
100101 & 000001
it will only look at last as bits in front is zero

'''
)
print('even')
a = 2
a&=1
print(a)
print()

print("************************************************************")
print(
f'''
to get rightmost bit out we have to do

num & -num

question 1: why this works?
answer:- when this happens, negative sign changes -num to its 2's complement.
        which then negates all 1 in normal num except rightmost one. giving
        only 1 or 0 if their are any.


question 2: what is 2' complement means?
answer :- two complement meaning -num, what happens underthe hood is it reverses the bits
            if 1 then to 0 and if 0 converts to 1. then adds one more bit to right. making
            2's complement.

2& -2 = {2& -2}
question 3: why above is giving two ?
answer :-  because rightmost bit is 2 itself, when converting it to binary it gives 10

12& -12 = {12& -12}

''')


print('counting bits using bitwise operations')

num = 19
count = 0
while num:
        num&= (num -1)
        #above will give not right most bit we need leastsignificat bit
        #then it will
        count+=1
        print(num)

print(count)

a = 1
b = 2
a^=b
b^=a
a^=b
print(a,b)


print('************************************************************************************')
print('power of check')
print('''
question 1: how to do it using bit wise operations?
answer :-   we will use and & operator here,  we will use bitwise & to compare number and number-1 with each other
                this will remove all the bits if the value is power of 2 , else 1.
''')
a = 4
print(4 & (4-1) == 0 and a > 0)

print('************************************************************************************')

print(' multiple of 2')
print('''
question 1: multiplying by 2
answer :-  just shifting is value just by one is equivalent too multiplying by 2.
''')

print(2<<1)

print('************************************************************************************')

print(' divide of 2')
print('''
question 1: devide by 2
answer :-  just shifting the value just by one to right is equivalent too dividing by 2.
''')

print(-2>>1)



