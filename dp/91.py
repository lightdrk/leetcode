def decoding(s :str) ->int:
    char_map = set(str(i) for i in range(1,27))
    length = len(s)
    memo = {}
    def recur(i):
        if i == length:
            return 1
        if s[i] == '0':
            return 0
        if i in memo:
            return memo[i]
        ans = 0
        if s[i:i+1] in char_map:
            ans+=recur(i+1)
        if i+1 < length and s[i:i+2] in char_map:
            ans+=recur(i+2)
        memo[i] = ans
        return ans

    return recur(0)
print(decoding("12"))

print(decoding("226"))

print(decoding("06"))

print(decoding("1206"))
test = "111111111111111111111111111111111111111111111"

print(decoding(test))


