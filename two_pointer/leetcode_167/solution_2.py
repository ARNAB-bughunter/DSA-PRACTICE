from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers) - 1
        while left_pointer < right_pointer:
            sum = numbers[left_pointer] + numbers[right_pointer]
            if sum == target:
                return [left_pointer+1, right_pointer+1]
            elif sum > target:
                right_pointer -= 1
            elif sum < target:
                left_pointer += 1
        return []
obj = Solution()
print(obj.twoSum([5,25,75], 100))