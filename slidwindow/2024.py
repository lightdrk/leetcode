test_case = ["TTFFF","TFTFTF", "TTFTFFFFFFT", "TFFT","TTFTTFTT"]


def maxConsecutive(s,k):
    left = 0
    T = 0
    F = 0
    count = 0
    for right in range(len(s)):
        if "T" == s[right]:
            T+=1
        else:
            F+=1
        while min(T,F)>k:
            if "T" == s[left]:
                T-=1
            else:
                F-=1
            left+=1
        count = max(count,right-left+1)

    return count


"""
now question adds complexity if we are asked to get us the indexs rather than count
"""

def maxConsecutive(s,k):
    left = 0
    T = 0
    F = 0
    count = 0
    index = (-1,-1)
    for right in range(len(s)):
        if "T" == s[right]:
            T+=1
        else:
            F+=1
        while min(T,F)>k:
            if "T" == s[left]:
                T-=1
            else:
                F-=1
            left+=1
        if count < right-left+1:
            count = right-left+1
            index = (left,right)
    return index 

for t in test_case:
    print(maxConsecutive(t,1))
