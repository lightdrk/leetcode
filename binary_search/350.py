'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.'''
from collections import Counter
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    n1 = Counter(nums1)
    n2 = Counter(nums2)
    ans = []
    for n in n1:
        if not n in n2:
            continue
        ans+=[n]*(min(n1[n],n2[n]))

    return ans

'''
array is sorted .
    '''

def ifSorted(nums1,nums2):
    ans = []

