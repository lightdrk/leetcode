'''

🧭 **Greedy Challenge – Intermediate+**

> **Problem:**
> There is a car that can travel **at most `fuel` kilometers** with a full tank.
> You are given a list of **`stations[] = [(dist_from_start, fuel_available)]`**, sorted by distance from the start.
> You start at position `0` with **0 fuel**.
> You can **refuel at any station**, and **each refueling takes time** (but doesn’t affect fuel capacity).
> Return the **minimum number of refueling stops** needed to reach a target distance.
> If it's impossible, return `-1`.

---

### 🔧 Example:

```python
target = 100
startFuel = 10
stations = [(10, 60), (20, 30), (30, 30), (60, 40)]
# Output: 2 (Refuel at 10 and 60)
```

---

### 📦 Constraints:

* All distances and fuel amounts are positive integers.
* `stations` is sorted by distance.
* Target ≤ 10^6, len(stations) ≤ 10^4
* You must minimize refuel **count**, not amount.

---

🔒 Don’t give final code yet.
Start by explaining:

1. What makes this greedy?
2. Why naive greedy may fail?
3. Then build strategy.

Keep answers in 2-line mode. I’ll respond accordingly.
'''
#######Not correct and complete#######
import heapq
#input arr is sorted based on distance from start or zero
#[(10,20),(30,50)]
def car_fuel(arr: list[tuple[int,int]], target: int, fuel: int):
    if target <= fuel:
        return 0
    maxHeap = []
    output = 0
    for dist, station in arr:
        if fuel < dist:
            fuel+= -(heapq.heappop(maxHeap))
            output+=1

        heapq.heappush(maxHeap, -station)
    while fuel < target and maxHeap:
        fuel+= -(heapq.heappop(maxHeap))
        output+=1
    
    print(fuel)
    if fuel < target:
        return -1

    return output

print(car_fuel([(10,30),(20,10)], 60,10))

print(car_fuel([(10,10),(20,20),(30,30)], 100, 10))
