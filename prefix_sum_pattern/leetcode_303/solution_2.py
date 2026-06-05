from typing import List
 
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_array = []
        self.nums = nums
        sum = 0
        for i in range(0, len(self.nums)):
            sum += nums[i]
            self.prefix_sum_array.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sum_array[right]
        left_sum = self.prefix_sum_array[left - 1] if left > 0 else 0
        return right_sum - left_sum

obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(2,5)
print(param_1)
