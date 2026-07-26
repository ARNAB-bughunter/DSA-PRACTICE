from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_array = []
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            prefix_sum_array.append(sum)
        
        print(prefix_sum_array)






obj = Solution()
print(obj.subarraySum([1,2,3], 3))