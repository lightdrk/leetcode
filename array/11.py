def area(height):
    area = 0
    left = 0
    right = len(height) - 1
    print(right)
    while left < right:
        h = height[left]
        if h > height[right]:
            h = height[right]
        n_area = right+1-(left+1)
        print(n_area)
        n_area*=h
        print(f"{h} x {right+1} - {left+1} ==",n_area)
        if area < n_area:
            area = n_area

        if height[left] == h:
            left+=1
        else:
            right-=1
    return area

print(area([1,8,6,2,5,4,8,3,7]))
