def canChange(start, target):
    # "_L__R__R_"
    # "_L", "L"
    # should have a letter
    # "L______RR"

    length = len(start)
    i = 0
    j = 0
    for i in range(length):
        if start[i] == "_":
            continue
        if start[i] == "L":
            for j in range(i, 0,-1):
                if target[j] == "_":
                    continue
                if start[i] != target[j]:
                    return False
        else:
            for j in range(i,length):
                if target[j] == "_":
                    continue
                if start[i] != target[j]:
                    return False
        return True

print(canChange("_L__R__R_","L______RR"))

print(canChange("R_L_","__LR"))
