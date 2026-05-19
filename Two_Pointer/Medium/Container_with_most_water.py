class Solution:
    def maxArea(self, height: List[int]) -> int:

        length,breadth = 0,0
        left,right = 0 ,len(height)-1
        water = 0
        max_water = 0

        while left < right:
            length = min(height[left],height[right])
            breadth = right - left
            water = length * breadth
            if height[left] > height[right]:
                right -= 1
            elif height[left] <= height[right]:
                left += 1
            max_water = max(max_water,water)
        return max_water
        