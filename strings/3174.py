def clearDigits(s: str) -> str:
    def clean(s):
        stack = []
        for i,char in enumerate(s):
            if char.isdigit():
                stack.pop()
                continue
            stack.append(char)
        return ''.join(stack)
    print(clean(s))
   # while not s.isalpha():
   #     s = clean(s)
   #     if s == '':
   #         return ''

print(clearDigits('abc'))
print(clearDigits('ab24'))
