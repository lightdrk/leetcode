def decrypt(code: list[int], k: int) -> list[int]:
    length = len(code)
    output = [0]*length
    sm_window = 0
    if k > 0:
        sm_window = 0
        while k:
            sm_window+=code[k%length]
            k-=1
        output[0] = sm_window
        for i in range(1,length):
            sm_window+= code[i%length] - code[(i-1)%length]
            output[i] = sm_window
    elif k < 0:
        sm_window = 0
        while k:
            sm_window+=code[k%length]
            k+=1
        output[0] = sm_window
        for i in range(1,length):
            sm_window+= code[i%length] - code[(i-1)%length]
            output[i] = sm_window
    return output


print(decrypt([5,7,1,4],3))
