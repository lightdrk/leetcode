'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

'''
#Thought 

'''
first thought i had was to use binary search to find , but when i thought about it 
i had to get the length of the array.,
then for me to find two values i had to 
do a loop inside that a binary search for number that equals to the target 
it would need n log n time complexity 

then i stopped here as it would be better to use hash_map for this ..

'''

#thought 

'''
hash_map can solve it in O (n) time complexity...
:)

'''

def twoSum(numbers,target):
    hash_map = {}
    for i,n in numbers:
        if target-n in hash_map:
            return [hash_map[target-n],i+1]
        hash_map[target-n] = i+1

    return [-1,-1]

'''
when i looked at the solution people were also using binary search or kinda two pointer and binary search combo
where would sum up l and r if greater sub r else l +1  as usually done in binary search
i did it..
had to check if array actually started from 1 :(;;;
using print(number[0])

                                        why this is better is because it has constant space rather than having to save all hash_map with n space complexity

)

for time complexity both are same . 
'''
def twoSum(numbers, target):
    l = 0
    right = len(numbers)-1
    while l <= right:
        ans  = numbers[right] - numbers[l]
        if ans == target:
            return [l+1,right+1]
        elif ans > target:
            right-=1
        elif ans < target:
            l+=1
    return [-1,-1]

