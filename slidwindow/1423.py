#[1,23,2,1] => can i choose 1 from the begning and then 2 from last or vice versa
#[1,23,2,1] => 1,1,23 ...
#4 - 0 -1 => 3, 4-1-1 =>2
def maxScore(cardPoints: list[int], k: int) -> int:
    length = len(cardPoints)
    if length == k:
        return sum(cardPoints)
    maxima = 0
    for i in range(k):
        print(max(cardPoints[i], cardPoints[length - i -1]))
        maxima +=max(cardPoints[i], cardPoints[length - i -1])
    return maxima

print(maxScore([1,2,3,4,5,6,1],3))
print(maxScore([1,1000,1],1))
