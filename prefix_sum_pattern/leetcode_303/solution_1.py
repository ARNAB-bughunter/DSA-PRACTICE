from typing import List
 
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(0, len(self.nums)):
            if left <= i <= right:                sum += self.nums[i]
        return sum

obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(2,5)
print(param_1)
