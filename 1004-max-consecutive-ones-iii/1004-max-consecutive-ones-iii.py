class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums)
        zero_count = 0
        max_count = 0

        while right < n:
            if nums[right] == 0:
                zero_count += 1

            right += 1

            while zero_count > k:
                if nums[left] == 1:
                    left += 1
                else:
                    zero_count -= 1
                    left += 1
            
            max_count = max(max_count,right-left)
        
        return max_count