class Solution:
    def isValid(self, s: str) -> bool:
        
        par_map = {"]":"[",")":"(","}":"{"}
        stack = []

        for ch in s:
            if ch in par_map:
                if stack and stack[-1] == par_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False

 


