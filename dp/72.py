'''
Edit Distance 

we have inputs (strings) two inputs -> word1 and word2

we need to convert word1 to word2

to convert we can do three operations 
1) insert a char 
2) delete a char
3) replace a char

we need to return minimum operations need .

recurision here

at single point do all the three operations.

hard thing would be how to do the operations itself

for insert i will not increate the index and move the index of word2 
for delete i will simple move idex by one
for replace i will move both



OR directly do the operations itself
for insert i will add the what is need in front of the string
for delete i will slice the string
for replace will similarly replace it
'''

'''
❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌

implemented with my idea ***this is wrong ****
what is wrong is that if we dont need to operations then ??
but here it is still counting..

def dist(word1, word2):
    l1 = len(word1)
    l2 = len(word2)

    def recur(word,i):
        if word == word2 :
            return 0
        if i >= l2 or i >= len(word):
            return float('inf')
        res = float('inf')
        if word[i] == word2[i]:
            i+=1
        else:
            if i < l2:
                res = min(1+recur(word[:i]+word2[i]+word[i:],i+1),res)

            if i < len(word):
                res = min(res, 1+recur(word[:i]+word[i+1:],i) )
                if i < l2:
                    res = min(1+recur(word[:i]+word2[i]+word[i+1:],i+1), res)


        return res 
    return recur(word1,0)

print(dist("horse","ros"))
print(dist("rose","ros"))
'''

def dist(word1,word2):
    l1 = len(word1)
    l2 = len(word2)

    def recur(i,j):
        '''
        here this is wrong because we will not get answer for 
        if l1 = 0 and l2 = 3 or any number 
        if l1 = any number and  l2  = is 0

        if i >= l1 or j >= l2:
            return 0 + (l1 - i)
        '''
        if i >= l1:
            return l2-j
        if j >= l2:
            return l1-i

        if word1[i] == word2[j]:
            return recur(i+1,j+1)
        
        else:
            return 1 + min(recur(i,j+1), recur(i+1,j), recur(i+1,j+1))

    return recur(0,0)


print(dist("horse","ros"))
print(dist("rose","ros"))
print(dist("intention","execution"))

