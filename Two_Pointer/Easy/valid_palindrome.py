class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = " ".join(ch for ch in s if ch.isalnum())
        
        n = len(strs)
        left = 0
        right = n-1
        
        while left < right:
            if strs[left].lower() != strs[right].lower():
                return False
            left += 1
            right -= 1
        return True

        