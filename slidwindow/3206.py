def numberOfAlternatingGroups(colors: list[int]) -> int:
    count = 0
    length = len(colors)
    for i in range(length):
        middle = colors[i]
        left = colors[(i-1)%length]
        right = colors[(i+1)%length]
        print(middle, (i+1), right)
        if middle != left and middle != right and left == right:
            count+=1
    return count

print(numberOfAlternatingGroups([0,1,0,0,1]))
