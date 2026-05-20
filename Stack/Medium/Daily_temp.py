class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        result = [0] * (len(temp))

        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
        return result