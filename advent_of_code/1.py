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
        if total == 0:
            count+=1
        sign = 1
        if a[0] == 'L':
            sign = -1
        val = total+int(a[1:])*sign
        total = val%100
    if total == 0:
        count+=1
    return count


string = '''
    L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
L32
L1
L-1'''
question = ''
with open('./input_1','r') as f:
    question = f.read().lstrip().rstrip().split()
print(func(question))
#print(func(string.lstrip().rstrip().split('\n')))
