def letterCombinations(digits):
    output = []
    num_map = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno", "7":"pqrs", "8":"tuv","9":"wxyz","0": " "}
    l = len(digits)
    def bk(n=0,s=''):
        if digits[n] == '#':
            new = s[:-1]
            new+=s[-1].capitalize()
            s = new
            n+=1
        if n == l:
            output.append(s)
            return


        for char in num_map[digits[n]]:
            bk(n+1,s+char)

    bk()
    return output

test = ["2#03#"]
for t in test:
    print(letterCombinations(t))
