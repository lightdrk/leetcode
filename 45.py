<<<<<<< Updated upstream
test_case = [[3,2,1,0,4],[1,2,0,0,5], [1,2,3,0,5], [2,3,1,1,4], [0], [0,1]]

def jumps(arr):
    l = len(arr)
    def dp(i):
        print(i, arr[i])
        if i+arr[i] >= l-1:
            return 0
        jump = float('inf')
        for ii in range(i+1,i+arr[i]):
            print(ii)
            steps = 1+dp(ii)
            print(steps)
            jump = min(jump, 1+dp(ii))
        return jump
    return dp(0)

for t in test_case:
    print(jumps(t))


=======
def jump(arr):
    l = len(arr)
    def dp(i):
        steps = i+arr[i]
        if steps >= l-1:
            return 1
        jumps = float('inf')
        for j in range(i+1,steps):
            jumps = min(jumps,1+dp(j))
        return jumps
    return dp(0)


test = [[2,3,1,1,4],[2,3,0,1,4]]

for t in test:
    print(jump(t))
>>>>>>> Stashed changes
