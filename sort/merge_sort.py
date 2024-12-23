def mine_merge_sort(nums):
    length = len(nums)

    if len(nums) <= 1 :
        return nums

    left = mine_merge_sort(nums[:length // 2])

    right = mine_merge_sort(nums[length//2:])

    sorted_list = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i = i + 1
        else:
            sorted_list.append(right[j])
            j = j + 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


print(mine_merge_sort([6,5,4,3,2,1]))

def merge(left, right):
    sorted_list = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i = i +1
        else:
            sorted_list.append(right[j])
            j = j + 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def merge_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    mid = length//2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left,right)



print(merge_sort([6,5,4,3,2,1]))
