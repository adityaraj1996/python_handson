'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

'''
To find the maximum length, we need a dict to store the value of count (as the key) and its 
associated index (as the value). We only need to save a count value and its index at the first
time, when the same count values appear again, we use the new index subtracting the old index 
to calculate the length of a subarray. A variable max_length is used to to keep track of the
current maximum length.
'''


class Solution:
    def findMaxLength(self, nums):
        dic = {0: 0}
        curr_sum = 0
        max_len = 0
        for index, num in enumerate(nums, 1):
            if num == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            if curr_sum in dic:
                max_len = max(max_len, index - dic[curr_sum])
            else:
                dic[curr_sum] = index
        return max_len


print(Solution().findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))

