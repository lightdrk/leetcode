import timeit

def bin_num(binary):
    number = 0
    for i,char in enumerate(binary[::-1]):
        if char == 'b':
            break
        if char == '1':
            number+=2**i
    return number

print(chr(bin_num('1111')))

def timing():
    binary = '0b11011011110110110111'  # start with a binary string prefix
    for _ in range(10):
        binary += '1'  # add a 1 to the binary string each time
        # Time the binary string conversion using timeit
        time_taken_bin = timeit.timeit(lambda: bin_num(binary), number=1)  # Time the bin_num conversion
        time_taken_int = timeit.timeit(lambda: int(binary, 2), number=1)  # Time the int() conversion
        # Print the results
        print(bin_num(binary) == int(binary,2))
        print(f"Binary-to-int time: {time_taken_bin} seconds")
        print(f"Int conversion time: {time_taken_int} seconds")
timing()
