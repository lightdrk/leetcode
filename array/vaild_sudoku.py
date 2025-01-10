def isValid(board):
    # we can in 3x3 box
    #this 3x3 box must have a num
    #9x9
    for i in range(0,9,3):
        for j in range(0,9,3):
            z = []
            for x in range(i,i+3):
                for y in range(j,j+3):
                    z.append((x,y))
            print(z)
isValid([])
