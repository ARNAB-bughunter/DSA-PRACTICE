from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = sorted([nums[i], nums[j], nums[k]])
                        if temp not in result:
                            result.append(temp)
        return result



obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))

