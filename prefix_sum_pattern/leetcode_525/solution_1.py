from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0

        def get_count(array: List[int]):
            one_count, zero_count = 0, 0
            for k in range(0,len(array)):
                if array[k] == 0:
                    zero_count += 1
                elif array[k] == 1:
                    one_count += 1
            if one_count == zero_count:
                return True
            return False
        
        for i in range(0, len(nums)):
            sub_array = []
            for j in range(i,len(nums)):
                sub_array.append(nums[j])
                if get_count(sub_array):
                    if len(sub_array) > max_len:
                        max_len = len(sub_array)
        return max_len



        
obj = Solution()
print(obj.findMaxLength([0,1,1]))
