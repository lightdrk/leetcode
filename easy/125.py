def isPalindrome(s):
    pal = ''
    lap = ''
    for char in s:
        if char.isalnum():
            char = char.casefold()
            pal+=char
            lap = char+lap

    return pal == lap

'''
here i thought of rather than doing pal == pal[::-1] it will save some time but .. did not work.
also i did not read the question properly ..., 
trying to optimize 
current timecompleixt is O (n)

'''
# when using pal == pal[::-1] rather than lap is better ???
'''
when we add value in lap it is just reading the value and reading them to lap 
so time complexity is  number of char in lap ( l ) and so it is doing it n times inside the n loop :(


that is why i  think is getting this issue. 

'''
def isPalindrome(s):
    pal = ''
    for char in s:
        if char.isalnum():
            pal+=char.casefold()

    return pal == pal[::-1]

