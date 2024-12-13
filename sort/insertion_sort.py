import timeit
import matplotlib.pyplot as plt

def mine_insertion_sort(nums):
    #if swap slow by 0.8 times the real one
    #[2,0,3,4,1]
    #[0,2,1,5,4,3]
    #[0,1,2,5,4,3]
    #[0,1,2,4,5,3]
    #[0,1,2,4,3,5]
    #[0,1,2,3,4,5]
    length = len(nums)
    for i in range(1,length):
        key = nums[i]
        while i > 0 and key < nums[i-1]:
            #nums[i], nums[i-1] = nums[i-1], nums[i] #swap slows done 
            nums[i] = nums[i-1]
            i = i - 1
        nums[i] = key
    return nums


def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key
    return nums

nums = [n for n in range(10000,0,-1)]
correct = nums[::-1]


t1 = timeit.timeit(lambda: print(correct == mine_insertion_sort(nums.copy())), number=5)
t2 = timeit.timeit(lambda: print(correct == insertion_sort(nums.copy())), number=5)

plt.bar(['t1', 't2'], [t1,t2], color=['blue', 'green'])
plt.show()
