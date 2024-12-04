def zigZag(s :str, row :int) ->str:
    matrix = []
    length = len(s)
    #divide to get no of words in a in a row
    words = length // row
    flip = 0
    for i in range(length):
        #append till words length 
        #start the reversal after reaching words length
        if len(matrix) < words:
            matrix.append(i)
        #idea here is if flip reaches end meaning 
        if flip == words-1:
            #start reducing it by one
            flip = flip - 1
            matrix[flip] = matrix[flip] + s[i]
        else:
            flip = flip + 1
            matrix[flip] = matrix[flip] + s[i]

        output = ""
        for string in matrix:
            output = output + string
        return output

print(zigZag('PAYPALISHIRING', 3))
