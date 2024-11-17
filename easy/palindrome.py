def isPalindrome(s: str) -> bool:
        s =s.replace(" ", "")
        s = s.casefold()
        new  = ""
        for i in s:
                print(i)
                if 97 <= ord(i) <= 112:
                        new = new+i
        print('reversed;', new[::-1])
        print('un changed',new)
        return new == new[-1:]

print(ord(0), ord(9))
print(isPalindrome("race a car"))
