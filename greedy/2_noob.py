'''

🧩 Greedy Interview Question #2: Minimum Number of Arrows to Burst Balloons
You are given an array of intervals where each interval represents the horizontal diameter of a balloon.
An arrow can be shot vertically and bursts all balloons that intersect that line.

🔹 Input:
points = [[10,16],[2,8],[1,6],[7,12]]

🔹 Output:
2

💡 Explanation:
You need to shoot the minimum number of arrows such that every balloon is burst.

One arrow can burst all balloons that overlap with its vertical path.

Constraints:
1 <= len(points) <= 10^5

points[i] = [start, end] with start <= end

No guarantee that points are sorted

All values are integers, no floats

Multiple intervals can be fully overlapping
'''

def burst(arr: list[list[int]]):
    if not arr:
        return 0
    arr.sort(key=lambda x: x[1])
    count = 1
    prev = arr[0][1]
    for start, end in arr[1:]:
        if prev < start:
            count+=1
            prev = end

    return count

print(burst([[1, 6], [2, 8], [7, 12], [10, 16]]))
print(burst([[1, 6]]))
print(burst([]))
