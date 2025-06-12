'''
first thing i did was solved the question for substring LOL



def longest(s):
    length = len(s)
    def expand(i,j):
        while i > -1 and j < length and s[i] == s[j]:
            i-=1
            j+=1

        return j-i-1
    output = 0
    for i in range(length):
        output = max(output, expand(i,i), expand(i,i+1))

    return output

'''

def longest(s):
    length = len(s)

    return output


print(longest('cbbd'))

print(longest('bbbab'))
