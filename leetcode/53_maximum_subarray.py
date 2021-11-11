from typing import List


class Solution:
    """The solution"""

    def maxSubArray(self, nums: List[int]) -> int:
        """Max sub-array"""
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:  # This builds up our dynamic programming array
                nums[i] += nums[i - 1]  # Kadane's algorithm
        return max(nums)  # The solution is the highest subarray value.
