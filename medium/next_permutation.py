def next_p(nums):
    length = len(nums)
    i = length -1
    j = 0
    #   |i-1| |i|
    #[1,|2  |,|3|] => 
    #we will be using two pointer 
    while i >0 and nums[i-1] >= nums[i]:
        i-=1

    print(i)
    i = i-1
    if i > 0:
        #j element 
        z = i+1
        j = i+1

        while z < length-1:
            z+=1
            if nums[i] < nums[z] and nums[z] < nums[j]:
                j = z

        #i,j
        nums[i],nums[j] = nums[j],nums[i]
    else:
        nums[:] = nums[::-1]

    print(nums)


next_p([5,1,1])
