def zigZag(s :str, row :int) ->str:
    if row == 1 or row > len(s):
        return s
    length = len(s)
    #divide to get no of words in a in a row
    matrix = [''] * row
    flip = 0
    reverse = 1
    for i in range(length):
        #append till words length 
        #start the reversal after reaching words length
        #idea here is if flip reaches end meaning 
        matrix[flip] = matrix[flip] + s[i]
        if flip == 0:
            reverse = False
        elif flip == row - 1:
            reverse = True

        if reverse:
            #start reducing it by one
            flip = flip - 1
        else:
            flip = flip + 1


    print(matrix)
    output = ""
    for string in matrix:
        output = output + string
    return output

print(zigZag('PAYPALISHIRING', 4))
