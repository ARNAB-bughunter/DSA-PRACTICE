from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        return max_area

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
