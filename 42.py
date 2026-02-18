test = [[2,1,1,2,3,0,0,3],[0,1,0,2,1,0,1,3,2,1,2,1]]

def trap(height):
    left = right = 0
    l = len(height)
    water = 0
    while left < l:
        ans = 0
        right = left+1
        while right < l and height[right] <= height[left]:
            ans+=(height[left]-height[right])
            print(f'height[left]{height[left]}- height[right] {height[right]}',ans)
            right+=1
        if height[right] > height[left]:
            water+=ans
        left = right
    print(water)
    return water
        

for t in test:
    trap(t)

# not correct answer above.

def trap(height):
    index = 0
    l = len(height)
    while index < l and height[index] > 0:
        index+=1
    while index < l:
        start = index
        val = height[index]
        while index < l and val >= height[index]: 

