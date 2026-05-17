# Two Sum

Prerequisites
- Hash map for value-to-index lookup
- Iteration with indices

Problem Summary
Given an array of integers and a target, return indices of the two numbers such that they add up to the target. You may assume exactly one solution and may not use the same element twice.

Intuition
If we know a number `num`, the only partner that completes the sum is `target - num`. While scanning left to right, we can store the indices of numbers we have already seen so we can match the current number instantly.

Optimal Approach: One-Pass Hash Map

Algorithm (matches current code)
1. Create an empty map: value -> index.
2. For each index `i` and value `num`:
   - Compute `complement = target - num`.
   - If `complement` exists in the map, return `[map[complement], i]`.
   - Otherwise store `map[num] = i`.

Code (current solution)
```python
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:

      hashmap = {}

      for i , num in enumerate(nums):
         complement = target - num

         if complement in hashmap:
            return [hashmap[complement],i]

         hashmap[num] = i
```

Detailed Code Walkthrough
- `hashmap` stores each value and the earliest index where it appears.
- For each `num`, we compute the only partner that can reach the target.
- If that partner was seen earlier, we return the stored index plus the current index.
- If not, we store the current number so future elements can match it.

Complexity
- Time: O(n) average
- Space: O(n)

Step-by-Step Workflow Example
Input: nums = [2, 7, 11, 15], target = 9
1. i=0, num=2, complement=7, hashmap = {} -> store {2: 0}
2. i=1, num=7, complement=2, hashmap has 2 -> return [0, 1]

Test Cases (input -> output)
- nums=[2, 7, 11, 15], target=9 -> [0, 1]
- nums=[3, 2, 4], target=6 -> [1, 2]
- nums=[3, 3], target=6 -> [0, 1]

Live Playable Example
Run the demo script to see the algorithm trace each step.
- Script: [Array&Hashing/Easy/two_sum_demo.py](Array&Hashing/Easy/two_sum_demo.py)
- Run: `python Array&Hashing/Easy/two_sum_demo.py`

Other Approaches

Brute Force
- Try every pair.
- Time: O(n^2), Space: O(1)

Common Pitfalls
- Storing the current number before checking the complement (can cause same-index reuse when target == 2*num).
- Forgetting to return immediately once a pair is found.
