def prodExSelf(nums):
    ''' time complexity will be n**2 '''
    output = []
    length = len(nums)
    for i in range(length):
        prod = 1
        for n in range(length):
            if not i == n:
                prod = prod * nums[n]
        output.append(prod)
    return output

def exSelf(nums):
    output = []
    product = 1
    for n in nums:
        product = product * n

    for n in nums:
        output.append(product//n)

    return output

print(prodExSelf([-1,1,0,-3,3]))
print(exSelf([-1,1,0,-3,3]))
