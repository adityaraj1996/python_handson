'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


class Solution:

    def singleNumber(self, nums):
        res = int(nums[0])
        for _ in range(1, len(nums)):
            res = res ^ int(nums[_])
        return res


nums = list(map(int, input()[1:-1].split(',')))
ob = Solution()
print(ob.singleNumber(nums))

