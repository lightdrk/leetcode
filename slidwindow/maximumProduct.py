'''
Given an integer numsay nums and an integer
𝑘
k, find a contiguous subnumsay of length
𝑘
k that has the maximum product and return this value.
'''

def maxProduct(nums: list[int], k: int) -> float:
    max_product = 1
    for i in nums[:k]:
        max_product = max_product * i
    product = max_product
    for i in range(len(nums) - k + 1):  # Correct the loop range here
        if nums[i] == 0:
            product = 1
            for n in nums[i+1:i+k]:
                product = product * n
        else:
            product = (product * nums[k+i-1]) / nums[i]  # Correct sliding window logic here
        max_product = max(max_product, product)  # Complete this line
    return max_product

print(maxProduct([2, 3, 4, 5, 6], 3))  # Expected Output: 120
print(maxProduct([-2, -3, -4, -5, -6], 3))  # Expected Output: -24
print(maxProduct([1, 0, -2, 3, 4, 0, -1], 2))  # Expected Output: 12
print(maxProduct([1, -2, 3, 0, -1, 2], 3))  # Expected Output: 6
print(maxProduct([10**5, 10**6, 10**5, 10**7], 2))  # Expected Output: 100000000000

#check for issue not working for zero
