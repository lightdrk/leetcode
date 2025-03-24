def test(nums):
    pair = 0
    for ni in nums:
        for nx in nums:
            print(ni, nx)
            if abs(ni - nx) <= min(ni,nx):
                if pair < ni^nx:
                    pair = ni^nx
    return pair


print(test([10,100]))
