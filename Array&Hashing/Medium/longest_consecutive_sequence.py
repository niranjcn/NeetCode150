class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = set(nums)
        
        max_out = 0
        
        for num in hashmap:
            if num - 1 not in hashmap:
                out = 1
                while num + out in hashmap:
                    out += 1 
                max_out = max(max_out,out)
            

        return max_out

                