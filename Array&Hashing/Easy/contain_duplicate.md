# Contains Duplicate

Prerequisites
- Hash set for membership checks
- Big-O basics

Problem Summary
Given an integer array, return true if any value appears at least twice; otherwise return false.

Intuition
The fastest way to detect a repeat is to remember everything we have already seen. If a value appears again, we can stop immediately.

Optimal Approach: Hash Set

Algorithm (matches current code)
1. Create an empty set `seen`.
2. For each `num` in `nums`:
   - If `num` is already in `seen`, return true (duplicate found).
   - Otherwise add `num` to `seen`.
3. If the loop ends, return false.

Code (current solution)
```python
class Solution:
   def hasDuplicate(self, nums: List[int]) -> bool:

      seen = set()
      for num in nums:
         if num in seen:
            return True
         seen.add(num)
      return False
```

Detailed Code Walkthrough
- `seen = set()` initializes a fast lookup structure for numbers encountered so far.
- The loop scans each value once.
- The membership check `if num in seen` is the key: it detects the first repeat and exits early.
- If the loop finishes without a match, no duplicates exist.

Complexity
- Time: O(n) average
- Space: O(n)

Step-by-Step Workflow Example
Input: nums = [1, 2, 3, 1]
1. seen = {}
2. num = 1 -> not in seen, add -> {1}
3. num = 2 -> not in seen, add -> {1, 2}
4. num = 3 -> not in seen, add -> {1, 2, 3}
5. num = 1 -> already in seen -> return true

Test Cases (input -> output)
- [1, 2, 3, 1] -> true
- [1, 2, 3, 4] -> false
- [7, 7] -> true
- [] -> false

Live Playable Example
Run the demo script to see the algorithm trace each step.
- Script: [Array&Hashing/Easy/contain_duplicate_demo.py](Array&Hashing/Easy/contain_duplicate_demo.py)
- Run: `python Array&Hashing/Easy/contain_duplicate_demo.py`

Other Approaches

Brute Force
- Compare every pair.
- Time: O(n^2), Space: O(1)

Sort Then Scan
- Sort, then check adjacent values.
- Time: O(n log n), Space: O(1) or O(n)

Common Pitfalls
- Forgetting to short-circuit when a duplicate is found.
- Using a list for membership checks, which turns the solution into O(n^2).
