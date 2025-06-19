'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


'''
'''
here i will do something like this if we have * i will use for loop for s till i find the value 
not similar to previous and then move both by one 

on getting . i will move simply by one as . is equal to any value ..
now what will i do with .* if this comes i will just check if their are any value after .* as anything will be true 
if we only have .* it will be true and if it starts with char then till we get to this .* we will move and if we have anything in last then
that mean last should be equal


'''

'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

''' 
solution is kind of if i get '.' or both i == j then we can simple move by one dp(i+1,j+1)
if i get '.*' then we can do two things 
 -> move j+2 by assume or can be becaus their is nothing to make it equal to 
## abc . a.*bc here we dont need .* 
another thing needs to be done simuteniously is we can move i+1 by one assuming thier might be a difff
'''


def isMatch(s,p):
    ls = len(s)
    lp = len(p)
    def dp(i=0,j=0):
        if j == lp:
            return i == ls
        
        first = i < ls and (p[j] == '.' or s[i] == p[j])
        if j+1 < lp and p[j+1] == '*':
            return dp(i,j+2) or (first and dp(i+1,j))

        return first and dp(i+1,j+1)
    return dp(0,0)

print(isMatch("aab", "c*a*b"))
