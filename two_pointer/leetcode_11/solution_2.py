from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pointer, right_pointer = 0, len(height) - 1

        while left_pointer < right_pointer:
            area = (right_pointer - left_pointer) * min(height[right_pointer], height[left_pointer])
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
            max_area = max(max_area, area)
        return max_area
        

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
