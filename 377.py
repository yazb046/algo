# 377. Combination Sum IV
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        map = {}
        def calc(nums, target):
            count = 0
            for n in nums:
                remainder = target - n
                if remainder == 0:
                    count += 1
                if n > 0 and remainder > 0 and (remainder not in map.keys()):
                    calc(nums, remainder)
                if remainder in map.keys():
                    count += map[remainder]
            map[target] = count
        calc(nums, target)
        return map[target]

print(Solution().combinationSum4([1,2,3], 4))
print(Solution().combinationSum4([2,5], 10))
print(Solution().combinationSum4([1], 0))
print(Solution().combinationSum4([0], 1))
print(Solution().combinationSum4([1], 100))
