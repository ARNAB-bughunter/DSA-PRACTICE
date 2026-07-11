from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate 'i' values
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1  # skip duplicate left values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1  # skip duplicate right values
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return result

obj = Solution()
print(obj.threeSum([1,2,0,1,0,0,0,0]))

