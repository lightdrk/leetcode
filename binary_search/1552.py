def maxDistance(position,m):
    position.sort()
    i = position[0]
    j = i-position[-1]
    for x in range(i,j+1):

