from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float("-inf")
        for i in range(len(nums) - k + 1):
            temp_result = 0
            for j in range(i, i+k):
                temp_result += nums[j]
            avg = temp_result / k
            result = max(result, avg)
        return result


obj = Solution()
print(obj.findMaxAverage([1,12,-5,-6,50,3], 4))