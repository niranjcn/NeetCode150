# Valid Anagram

Prerequisites
- Hash map for frequency counting
- Basic string iteration

Problem Summary
Given two strings s and t, return true if t is an anagram of s, otherwise false.

Intuition
Two strings are anagrams if every character appears the same number of times in both strings. We count characters in `s`, then make sure `t` consumes those counts exactly.

Optimal Approach: Hash Map Frequency Count

Algorithm (matches current code)
1. If lengths differ, return false.
2. Build a map of char -> count for `s`.
3. For each char in `t`:
   - If the char is not in the map, return false.
   - Decrement its count; if it becomes negative, return false.
4. If the loop ends, return true.

Code (current solution)
```python
class Solution:
   def isAnagram(self, s: str, t: str) -> bool:

      if len(s) != len(t):
         return False

      count = {}
      for ch in s:
         count[ch] = count.get(ch,0) + 1

      for c in t:
         if c not in count:
            return False
         count[c] -= 1
         if count[c] < 0:
            return False

      return True
```

Detailed Code Walkthrough
- The length check is a quick early exit: different lengths cannot be anagrams.
- The first loop builds counts for every character in `s`.
- The second loop consumes those counts using `t`.
- If any character is missing or overused, the answer is false.

Complexity
- Time: O(n)
- Space: O(k), where k is the number of distinct characters in `s`

Step-by-Step Workflow Example
Input: s = "anagram", t = "nagaram"
1. count after s: {a:3, n:1, g:1, r:1, m:1}
2. consume t in order; no bucket drops below 0
3. return true

Test Cases (input -> output)
- s="anagram", t="nagaram" -> true
- s="rat", t="car" -> false
- s="aabb", t="bbaa" -> true
- s="abc", t="ab" -> false

Live Playable Example
Run the demo script to see the algorithm trace each step.
- Script: [Array&Hashing/Easy/Valid_Anagram_demo.py](Array&Hashing/Easy/Valid_Anagram_demo.py)
- Run: `python Array&Hashing/Easy/Valid_Anagram_demo.py`

Other Approaches

Sorting
- Sort both strings and compare.
- Time: O(n log n), Space: O(n)

Fixed-Size Count Array (for lowercase a-z)
- Use an array of size 26 instead of a map.
- Time: O(n), Space: O(1)

Common Pitfalls
- Skipping the length check, which can waste time or miss false cases.
- Forgetting to handle characters that are not in the map.
