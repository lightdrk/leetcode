def generate(n):
    output = []
    def bk(par, l, r):
        if n*2 == l + r:
            output.append(par)

        if n > l:
            bk(par+'(',l+1,r)
        if l>r:
            bk(par+')',l,r+1)
    bk('',0,0)
    return output

print(generate(3))
