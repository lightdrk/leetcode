'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

'''

'''
l = lenght

for loop
then expand from center (i)
output for this would be (i,j) start till end , and this 
would be or meaning would be i == j at every point
so  i would assume all substrings that are palandrome i as a center would be 
(j-i)
then expand from center (i,i+1)
simlarly for even exapnd 
(j-i)
i will sum both (j-i)odd + (j-i) even


return sum

expand func()
count = 0
while i > -1 and j < length and s[i] == s[j] :
    i-=1
    j+=1
    count+=1

return count

'''
test_case = [('a', 1), ('aaaaa', 15), ('abbbba', 13) ]

def func(s: str)->int:
    l = len(s)
    def expand(i,j):
        count = 0
        while i > -1 and j < l and s[i] == s[j]:
            i-=1
            j+=1
            count+=1
        return count

    count = 0
    for i in range(l):
        count+= expand(i,i) + expand(i,i+1)

    return count

for q,a in test_case:
    ans = func(q)
    print(ans, end='isValid ?')
    print(ans== a)




test_case = ['a', 'aaaaa', 'abbbba' ]

def func(s: str)->set:
    l = len(s)
    def expand(i,j):
        while i > -1 and j < l and s[i] == s[j]:
            output.add(s[i:j+1])
            i-=1
            j+=1
    output = set()
    for i in range(l):
        expand(i,i)
        expand(i,i+1)
    return output

for q in test_case:
    print(func(q))

