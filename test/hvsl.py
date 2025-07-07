import random
import time


word = list(range(100000))
words =  set(range(1000000))


s = time.time()
for i in range(100000):
    if i in word:
        print(f"\rProgress: {i}/100000", end='', flush=True)
e = time.time()

print("for array: ",e - s)



s = time.time()
for i in range(100000):
    if i in words:
        print(f"\rProgress: {i}/100000", end='', flush=True)
e = time.time()

print("for set: ",e - s)


