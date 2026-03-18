'''
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.
'''
test_case = ["abcabc", "aaacb", "caabbac"]


'''
we are currently doing it with taking or as we know that current setup if window length that is rescticted to {a,b,c} we are 
adding (l-right) as current setup is valid and we do not care if anything on right side after right adds more or less ,
as we already have valid condition already
and we then iterate till we get to the point where vaild scenerioa breaks and as we have already added (l-right ) this includes 
all the condition before window becomes invalid 

'''
def numberOfSub(s):
    count = 0
    window = {}
    left = 0
    l = len(s)
    for right in range(len(s)):
        char = s[right]
        if char in {'a','b','c'}:
            window[char] = window.get(char,0)+1
        while len(window)==3:
            print(f"right -> {right}")
            count+=(l-right)
            if s[left] in window:
                window[s[left]]-=1
            if window[s[left]] == 0:
                del window[s[left]]
            left+=1
    return count


def numberOfSub_v2(s):
    count = 0
    a = b = c = 0
    left = 0
    l = len(s)
    for right in range(l):
        if s[right] == 'a':
            a+=1
        elif s[right] == 'b':
            b+=1
        elif s[right] == 'c':
            c+=1
        while a >0 and b>0 and c>0:
            if s[right] == 'a':
                a-=1
            elif s[right] == 'b':
                b-=1
            elif s[right] == 'c':
                c-=1
            left+=1
        count+=(left)
    return count



for t in test_case:
    print(numberOfSub(t))
    print(numberOfSub_v2(t))
