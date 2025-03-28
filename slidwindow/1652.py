def decrypt(code: list[int], k: int) -> list[int]:
    length = len(code)
    if k == 0:
        return [0]*length
    output = [0]*length
    mv = 1
    if k < 0:
        mv = -1
        k = -k
    for i in range(length):
        for j in range(1,k+1):
            print(i+j+1)
            output[i]+=code[(i+j*mv)%length]
    return output


print(decrypt([5,7,1,4],3))
print(decrypt([3,2,5,7,6], 3))

print(decrypt([2,4,9,3], -2))
