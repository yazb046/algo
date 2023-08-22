from typing import List
import math
import cProfile
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
# create global variable to store MAX integer value
        MAX_INT = math.inf

# checker to handle case when amount = 0
        if amount == 0:
            return 0

# memoization: a map-type variable to write/read step values
        stepsValues = {}
        def solve(amount):
            minValue = MAX_INT
            for coin in coins:
                remainder = amount - coin
                if remainder < 0:
                    continue
                if remainder == 0:
# write step value directly to map
                    stepsValues[coin] = 1
# use return only to interrupt a loop and a recursion
                    return
                temp = MAX_INT
                if remainder not in stepsValues:
                    solve(remainder)
# use if, avoid else to make possible to get map value
# after getting out of a recursion
                if remainder in stepsValues:
                    temp = stepsValues[remainder]
                minValue = min(temp + 1, minValue)
            stepsValues[amount] = minValue
        solve(amount)
# checker to handle case when result == MAX_INT
        return -1 if stepsValues[amount] == MAX_INT else stepsValues[amount]
cProfile.run("print(Solution().coinChange([1,2,5], 100))")
print(Solution().coinChange([1,2,5], 100))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([2], 0))