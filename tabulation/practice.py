'''

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

    '''

def func(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

'''
def climb(n):
    if n <= 2:
        return n
    return climb(n - 1) + climb(n - 2)
'''

def func1(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

'''
def minCost(i, cost):
    if i <= 1:
        return 0
    return min(minCost(i - 1, cost) + cost[i - 1],
               minCost(i - 2, cost) + cost[i - 2])

tabulation

dp = []*len()

for i in range()

'''














'''

Perfect — here's what we'll do:

I'll give you the **recursive (top-down)** version (with or without memoization) of each problem, and you can **practice converting it into tabulation (bottom-up)**. This is the best way to internalize how subproblem structure works.

---

### 🔰 1. Fibonacci Numbers (Basic)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

### 🔰 2. Climbing Stairs

```python
def climb(n):
    if n <= 2:
        return n
    return climb(n - 1) + climb(n - 2)
```

---

### 🔰 3. Min Cost Climbing Stairs

```python
def minCost(i, cost):
    if i <= 1:
        return 0
    return min(minCost(i - 1, cost) + cost[i - 1],
               minCost(i - 2, cost) + cost[i - 2])
```

---

### 🧱 4. House Robber

```python
def rob(i, nums):
    if i < 0:
        return 0
    return max(rob(i - 1, nums), rob(i - 2, nums) + nums[i])
```

---

### 🧱 5. Coin Change (Min Coins)

```python
def coinChange(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    return min(coinChange(coins, amount - c) + 1 for c in coins)
```

---

### 🧠 6. Longest Common Subsequence (LCS)

```python
def lcs(i, j, s1, s2):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + lcs(i + 1, j + 1, s1, s2)
    return max(lcs(i + 1, j, s1, s2), lcs(i, j + 1, s1, s2))
```

---

### 🧠 7. Edit Distance

```python
def edit(i, j, s1, s2):
    if i == len(s1):
        return len(s2) - j
    if j == len(s2):
        return len(s1) - i
    if s1[i] == s2[j]:
        return edit(i + 1, j + 1, s1, s2)
    return 1 + min(
        edit(i + 1, j, s1, s2),    # delete
        edit(i, j + 1, s1, s2),    # insert
        edit(i + 1, j + 1, s1, s2) # replace
    )
```

---

### 🧠 8. 0/1 Knapsack

```python
def knapsack(i, W, wt, val):
    if i == 0 or W == 0:
        return 0
    if wt[i-1] > W:
        return knapsack(i - 1, W, wt, val)
    return max(
        knapsack(i - 1, W, wt, val),
        knapsack(i - 1, W - wt[i-1], wt, val) + val[i-1]
    )
```

---

### 🧠 9. Subset Sum

```python
def subsetSum(i, target, nums):
    if target == 0:
        return True
    if i == 0:
        return nums[0] == target
    not_pick = subsetSum(i - 1, target, nums)
    pick = False
    if nums[i] <= target:
        pick = subsetSum(i - 1, target - nums[i], nums)
    return pick or not_pick
```

---

### 🧗‍♂️ 10. Matrix Chain Multiplication

```python
def mcm(i, j, dims):
    if i == j:
        return 0
    min_cost = float('inf')
    for k in range(i, j):
        cost = (mcm(i, k, dims) +
                mcm(k + 1, j, dims) +
                dims[i - 1] * dims[k] * dims[j])
        min_cost = min(min_cost, cost)
    return min_cost
```

---

Would you like more problems or start converting these first?

I can also check your tabulated version when you're done with one!

    '''
