def getPermutation(n, k):
    # List of numbers to permute
    nums = [str(i) for i in range(1, n + 1)]
    result = []
    # This will store the current k-th permutation in result
    # We use this to track how many permutations we have found
    k_counter = [0]
    def backtrack(current):
        # If we've found a permutation, increment the counter
        if len(current) == n:
            k_counter[0] += 1
            if k_counter[0] == k:
                result.append(''.join(current))
            return
        # Try all possible numbers in the current position
        for i in range(len(nums)):
            if nums[i] not in current:
                current.append(nums[i])
                backtrack(current)
                current.pop()  # Backtrack
    # Start backtracking
    backtrack([])
    return result[0] if result else ""

# Example usage:
n = 3
k = 5
print(getPermutation(n, k))  # Output: "231"


