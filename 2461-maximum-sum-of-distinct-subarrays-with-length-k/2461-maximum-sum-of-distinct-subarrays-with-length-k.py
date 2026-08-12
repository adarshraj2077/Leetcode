class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        window_sum = sum(nums[:k])
        max_sum = 0

        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        if len(freq) == k:
            max_sum = window_sum

        for i in range(k, len(nums)):

            freq[nums[i-k]] -= 1

            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]

            freq[nums[i]] = freq.get(nums[i], 0) + 1

            window_sum = window_sum - nums[i-k] + nums[i]

            if len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum