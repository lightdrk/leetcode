'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

'''
#psudeo code
'''
dfs structure -> {
    points to remmenber 
    * choices we made per tree should not affect other disions meaning if we had taken a path we can take it again 
        if we are in different desision 
    * we need to make desision making/

    #recursive 
        params (i,j, visited , index of string)
        check if index is last 
            return true
        update visited with curr i,j
        loop
            check for if next char is valid 
                do call recursive call (i,j updated, visited,update index )
                if true :
                    return true
        return False
    #iterative 
        use stack
        loop stack:
            pop from stack
            check for index is last  return True
            loop over the choices 
                append to stack if valid choices 
                (appending to stack , we append a new visited set copy deep copy, index)

        return False


}

interate over grid
    if we get starting char of string at the iteration
        do dfs
        if ans true return true else continue


'''



