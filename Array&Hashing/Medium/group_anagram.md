# Group Anagrams

Prerequisites
- Hash map for grouping
- String sorting or character counting

Problem Summary
Given an array of strings, group the anagrams together. You may return the answer in any order.

Intuition
Anagrams share a common signature. If two words have the same signature, they belong in the same group. A simple signature is the sorted characters of the word.

Optimal Approach: Sorted Key

Algorithm (matches current code)
1. Create an empty map: `sorted_word -> list of words`.
2. For each word in `strs`:
   - Compute `sorted_word = "".join(sorted(word))`.
   - Append `word` to the list for `sorted_word`.
3. Return all map values.

Code (current solution)
```python
class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      grp_anagram = {}

      for word in strs:
         sorted_word = "".join(sorted(word))

         if sorted_word in grp_anagram:
            grp_anagram.get(sorted_word).append(word)
         else:
            grp_anagram[sorted_word] = [word]

      return [word for word in grp_anagram.values()]
```

Detailed Code Walkthrough
- `grp_anagram` maps each signature to the group of words sharing it.
- Sorting a word makes its letters canonical, so all anagrams produce the same key.
- Each word is appended to its signature group.
- The return statement collects all groups into a list.

Complexity
- Time: O(n * m log m), where `m` is max word length
- Space: O(n * m)

Step-by-Step Workflow Example
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
1. "eat" -> key "aet" -> {"aet": ["eat"]}
2. "tea" -> key "aet" -> {"aet": ["eat", "tea"]}
3. "tan" -> key "ant" -> {"aet": [...], "ant": ["tan"]}
4. "ate" -> key "aet" -> {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
5. "nat" -> key "ant" -> {"aet": [...], "ant": ["tan", "nat"]}
6. "bat" -> key "abt" -> {"aet": [...], "ant": [...], "abt": ["bat"]}
Result: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Test Cases (input -> output)
- ["eat", "tea", "tan", "ate", "nat", "bat"] -> groups of anagrams
- [""] -> [[""]]
- ["a"] -> [["a"]]
- ["ab", "ba", "abc", "cba"] -> [["ab", "ba"], ["abc", "cba"]]

Live Playable Example
Run the demo script to see the algorithm trace each step.
- Script: [Array&Hashing/Medium/group_anagram_demo.py](Array&Hashing/Medium/group_anagram_demo.py)
- Run: `python Array&Hashing/Medium/group_anagram_demo.py`

Other Approaches

Count Signature (for lowercase a-z)
- Use a 26-length count tuple as the key.
- Time: O(n * m), Space: O(n * m)

Common Pitfalls
- Using a list as a dictionary key (must be immutable, like tuple or string).
- Forgetting that output order is arbitrary; tests should accept any group order.
