def inclusion(s1 :str, s2: str) -> bool:
    l1 = len(s1)
    l2 = len(s2)
    print(l1, l2)
    if l1 > l2:
        return False
    window = {} #using hash map as char can be n times
    for char in s1:
        if not char in window:
            window[char] = 0
        window[char]+=1
    for i in range(l2-l1+1):
        if s2[i] in window:
            t_w = {}
            tmp = 0
            while tmp < l1:
                char = s2[i+tmp]
                if not char in window:
                    break
                if not char in t_w:
                    t_w[char] = 0
                t_w[char]+=1
                tmp+=1
            print(t_w)
            if t_w == window:
                return True
    return False
print(inclusion('ab', 'mngdba'))
print(inclusion('adc', "dcda"))
