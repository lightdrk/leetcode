print('Subtraction , like human bit by bit')

from_ = int(input('Subtract from: '))
to_ = int(input('subtract By: '))

carry = 0
bin_f = f"{from_:b}"
bin_t = f"{to_:b}"
idx = 0
output = ''
carry = '0'
for char in bin_f[::-1]:
    if cha
