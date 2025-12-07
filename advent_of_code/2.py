'''
l mean , it goes from max to low 
r min to max 
and the array is connected meaning circular

starting is from 50

L 68 -> 68 - 50 -> 18 in array will be 82
R 68 -> 50+68 -> 118%100 -> 18
----------------------------------------
L 30 -> 82-30 -> 

'''

def func(arr):
    count = 0
    total = 50
    for a in arr:
        print()
        print('count -> ',count)
        if total == 0:
            count+=1 
        sign = 1
        num = int(a[1:])
        if a[0] == 'L':
            sign = -1
        if num > 100 or num < -100:
            print('num is greater than 100 ')
            count+= (num//100)
            num%=100
        print(f'num -> {num} total -> {total}', count)
        val = total+num*sign
        if (val < 0 or val > 100) and total != 0:
            print(f'adding 1 to count {count} as it crosses 0 ')
            count+=1
        total = val%100

    if total == 0:
        count+=1
    return count


string = '''
L680
L300
R48
L5
R60
L55
L1
L99
R14
L82
'''
question = ''
with open('./input_1','r') as f:
    question = f.read().lstrip().rstrip().split()
print(func(question))
'''
print(func(string.lstrip().rstrip().split('\n')))
    '''
