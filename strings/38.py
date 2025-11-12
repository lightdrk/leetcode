def count_say(n):
    def rec(n):
        if n == 1:
            return '1'
        next = rec(n-1)
        build = ''
        counter = 0
        prev = next[0]
        for c in next:
            if c != prev:
                build+= str(counter)+prev
                counter = 0
                prev = c
            counter+=1
        build+=str(counter)+prev
        return build
    return rec(n)
test_case = [1,2,3,4,5]
for t in test_case:
    print(count_say(t))



