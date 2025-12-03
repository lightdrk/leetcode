def totalF(fruits):
    left = 0
    counter = {}
    ans = 0
    l = len(fruits)
    for right in range(l):
        print(counter, fruits[right])
        fruit = fruits[right]
        if fruit not in counter:
            counter[fruit] = 0
        counter[fruit]+=1
        
        while len(counter) > 2:
            counter[fruits[left]]-=1
            if counter[fruits[left]] <= 0:
                del counter[fruits[left]]
            left+=1
        if ans < right-left+1:
            ans = right-left+1
    return ans



test_case = [[1,1,2,1,3,3,4,1],[1,1,1,1],[1,2,2,1,3]]

for t in test_case:
    print(totalF(t))
