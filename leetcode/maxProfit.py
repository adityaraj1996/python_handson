class Solution:
    def maxprof(self, prices):
        return sum([b - a for a, b in zip(prices, prices[1:]) if b-a > 0])


print(Solution().maxprof([7,1,5,3,6,4]))