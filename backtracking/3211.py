test_case = [1,2,3,4]

def validStrings(n):
    """
    2 -> 00
    """
    ans = []
    def bk(i:int,a:str):
        if '00' in a:
            return

        if i == n:
            ans.append(a)
            return

        bk(i+1,a+'0')
        bk(i+1,a+'1')
    bk(0,'')
    return ans

for n in test_case:
    print(validStrings(n))
