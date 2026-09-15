class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        min_len = n + 1
        curr_sum = 0

        while r < n:
            curr_sum += nums[r]

            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1

            r += 1

        if min_len == n + 1:
            return 0

        return min_len