'''

📝 Activity Selection Problem:
You are given a list of n activities, where each activity is represented as a pair [start, end].
Your task is to select the maximum number of non-overlapping activities you can perform.

🧩 Constraints:

Each activity takes place in the interval [start, end).

Activities must be performed sequentially, and you cannot overlap any two.

Return the maximum number of non-overlapping activities.

📦 Input: A list of activities = [[start1, end1], [start2, end2], ...]
📤 Output: An integer — the maximum number of non-overlapping activities.
'''
def overlap(arr: list[list[int]]):
    arr.sort(key=lambda x: x[1])
    counter = 1
    prev = arr[0][1]
    for start, end in arr[1:]:
        if prev > start:
            continue
        counter+=1
        prev = end

    return counter

test_cases = [
[[1, 3], [2, 4], [3, 5], [0, 6], [5, 7], [8, 9], [5, 9]],
[[0,0]]

]
for idx, test in enumerate(test_cases):
    print(f'{idx }->>',overlap(test))
