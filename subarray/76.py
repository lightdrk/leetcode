def sub(s,t):
    t_map = {}
    for T in t:
        if T in t_map:
            t_map[T] += 1
        t_map[T] = 1

    sub_strings = []
    for i in range(len(s)):
        for n in range(i+1,len(s)):
            window_map = {}
            add = True
            for char in s[i:n]:
                if char in window_map:
                    window_map[char] = window_map[char] + 1
                window_map[char] = 1

            for ii in t_map.items():
                if ii in window_map and window_map[ii] < t_map[ii]:
                    add = False
                    break
            if add:
                sub_strings.append(s[i:n])
    return sub_strings

print(sub("BABCD", "BC"))
