def binary(num):
    b = ''
    while num:
        b = str(num%2) + b
        num//=2

    return b
print(binary(13))
