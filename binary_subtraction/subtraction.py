print('Subtraction , like human bit by bit')

from_ = int(input('Subtract from: '))
to_ = int(input('subtract By: '))

carry = 0
bin_f = f"{from_:b}"
bin_f = [char for char in bin_f]
print(bin_f)
bin_t = f"{to_:b}"
length = len(bin_f)
lt = len(bin_t) - 1
print(bin_t, lt)
output = ''
borrow = 0
for i in range(length-1,-1,-1):
    if lt == -1:
        break

    if bin_f[i] == '0' and bin_t[lt] == '1':
        while bin_f[i] != 1:
            i-=1
            borrow+=1
        bin_f[i] = 2
        while borrow > 0:
            bin_f[i+1] = '1'
            borrow-=1
        output = '1' + output
    elif bin_f[i] == bin_t[lt]:
        output = '0' + output
    elif bin_f[i] == '1' and bin_t[lt] == '0':
        output = '1' + output
    lt-=1

print(output)
