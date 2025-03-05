def letterCombinations(digits: str):
    if not digits:
        return []
    hash_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    output = []
    length = len(digits)
    def bk(curr,idx):
        if idx == length:
            output.append(curr)
            return
        for char in hash_map[digits[idx]]:
            bk(curr+char, idx+1)
    bk('',0)
    return output

print(letterCombinations(''))
