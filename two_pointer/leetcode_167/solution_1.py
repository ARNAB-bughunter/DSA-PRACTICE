from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []

obj = Solution()
print(obj.twoSum([5,25,75], 100))