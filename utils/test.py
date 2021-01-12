# class Solution:
#     def twoSum(self, nums, target: int):
#         nums_length = len(nums)
#         for i in range(nums_length):
#             for j in range(i+1, nums_length):
#                 if target == nums[i] + nums[i + j]:
#                     print([i, i + j])
#                     break
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashtable = dict()
        # for i, num in enumerate(nums):
        #     if target - num in hashtable:
        #         return [hashtable[target - num], i]
        #     hashtable[nums[i]] = i
        # return []
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i


s = Solution()
print(s.twoSum([3, 2, 4], 6))
