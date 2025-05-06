def longestPalindrome(s :str)->str:
    length = len(s)
    ans = ''
    cache = set()
    lengths = -1
    for i in range(length):
        for j in range(i,length):
            pl = s[i:j+1]
            if pl in cache:
                continue
            if pl != pl[::-1]:
                continue
            cache.add(pl)
            if lengths < j-i+1:
                lengths = j-i+1
                ans = pl
    return ans


print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))
test = "xaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"

print(longestPalindrome(test))


def optimized(s :str) -> str:
    def expand(i,j):
        while i>=0 and j<length:
            if s[i] != s[j]:
                return (i+1,j)
            i-=1
            j+=1
        return (i+1,j)

    length = len(s)
    ans = ''
    s_length = -1
    for i in range(length):
        n,j = expand(i,i)
        n2,j2 = expand(i,i+1)
        if s_length < j-n:
            s_length = j-n
            ans = s[n:j]
        if s_length < j2-n2:
            s_length = j2-n2
            ans = s[n2:j2]
    return ans

print(optimized('babad'))
print(optimized('aaaaaaaa'))

print(optimized('cbbd'))
print(optimized(test))


