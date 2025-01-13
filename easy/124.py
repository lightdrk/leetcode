def isPalindrome(s):
    word = ''
    for char in s:
        ascii_val = ord(char)
        if 65 <= ascii_val and ascii_val <= 90:
            word += chr(ascii_val+32)
        elif 97 <= ascii_val:
            word += char
    return word[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))

def isPal(s):
    s = s.lower()
    print(s)

print(isPal("A man, a plan, a canal: Panama"))
