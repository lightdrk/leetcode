def minOperation(boxes: str):
    l = len(boxes)
    ans = [0]*l
    for i in range(l):
        count = 0
        for j in range(l):
            if boxes[j] == 1:
                count = j-i
