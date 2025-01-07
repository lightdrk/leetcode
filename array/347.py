def counting(nums,k):
    counter = {}
    for n in nums:
        if not n in counter:
            counter[n] = 0
        counter[n]+=1
    print(counter)
    bucket = [[] for _ in range(len(nums)+1)]
    for c in counter:
        bucket[counter[c]].append(c)
    print(bucket)

    result =[]
    for b in bucket[::-1]:
        for v in b:
            print(v)
            result.append(v)
    print(result[:k])
counting([-1,-1],1)

