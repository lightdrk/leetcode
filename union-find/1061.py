'''
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2

    '''
'''
create conectivity array , where we can get lowest ranking lexicographically chars,
a,b,c --> c,d,e
a== c
a b a
e e d
a == b 
d == a

ok so we have connectivity with s1 and s2 we need to convert baseStr based on what we have after s1 ,


plan:

we can use hash_map here and create equivalency , so let it be parent , or we can create a workd 27 word array 
then do ranking based on that , or we might not need any 

we have array [......]
with index being string nums , now we have a == c, we find nothing , so we also check rank or simply do count lexo and here we can do smallest per value which will give us then samllest as whole greedy is also their,  

    '''


'''
1. uneven strings ? like s1 == 1 and s2 = 2  in lenght i am talking about
ans: will be equal always .
2. what happens when we have no match in baseStr ?? we return that as it is right ?
ans: yes 
3. all lower case ? yes well wouldnt matter in a way as we will still have a constant string length either 27 or 2*27,

4. another question if we had more than like all utf chars thing then would have used hash_map.
5. also from what i think my algo that i have written will work for utf chars too i guess , but thats outof scope for now ,
6. if we have emtry s1 and s2 are their any constains for these being empty ? no 
'''

''''
edge cases lets think about,.


1. what if we have s1 and s2 but baseStr already is in lowest lexicographically. then what will this work ? 
ans: so it should return baseStr without change if it is the smallest itself ,... and yess my approach works

2. 



    '''

edge_case = [['abcdefg','abcdeag', 'aaaaaa'], ['','','empty'], ['some', 'thing', ''], ['avd','ncd', 'xzy'], ["parker", "morris", "parser"], ["hello", "world", "hold"], ["leetcode","programs","sourcecode"]]


def func(s1,s2,baseStr)->str:
    ans = ''
    #this will generate our needed data 
    parent = [chr(i) for i in range(97,123)]
    #rank = [0]*26
    idx = lambda x: ord(x)-97
    def find(x: str):
        if parent[idx(x)] != x:
            parent[idx(x)] = find(parent[idx(x)])
        return parent[idx(x)]
    
    def union(x,y):
        rootX = find(x)
        rootY = find(y)

        if idx(rootX) < idx(rootY):
            parent[idx(rootY)] = rootX
            return
        parent[idx(rootX)] = rootY

    for x,y in zip(s1,s2):
        union(x,y)

    for char in baseStr:
        ans+=find(char)

    return ans 


for s1,s2,baseStr in edge_case:
    print(func(s1,s2,baseStr))


print(func("abcdefghijklmnopqrstuvwxyz", 
           "bcdefghijklmnopqrstuvwxyza", 
           "leetcode"))  
# Expected: "aaaaaaaa"  
# because everything links into one cycle, smallest = "a"
