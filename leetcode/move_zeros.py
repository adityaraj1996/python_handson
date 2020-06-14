import time


class Solution:
    def move_0(self, nums):
        for _ in range(nums.count(0)):
            nums.append(nums.pop(nums.index(0)))

        return nums


start_time = time.time()
print(Solution().move_0([0, 1, 0, 3, 12]))
print(f"the execution time is {time.time() - start_time}")