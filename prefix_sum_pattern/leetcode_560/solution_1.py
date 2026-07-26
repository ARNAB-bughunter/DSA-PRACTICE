from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(0, len(nums)):
            sub_array = []
            for j in range(i,len(nums)):
                sub_array.append(nums[j])
                if sum(sub_array) == k:
                    res += 1
        return res





obj = Solution()
print(obj.subarraySum([1,2,3], 3))