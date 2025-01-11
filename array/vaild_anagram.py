def valid(s,t):
    hash_map = {}
    for i,j in zip(s,t):
        if not i in hash_map:
            hash_map[i]=0
        if not j in hash_map:
            hash_map[j]=0

        hash_map[i]+=1
        hash_map[j]-=1
    print(hash_map)


valid('mohi','tohim')
valid('a','ab')
