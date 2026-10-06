class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        count = 0

        for i in range(1,len(nums)-1):
            if nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            while j<len(nums) and nums[j] == nums[i]:
                j += 1
            
            if j == len(nums):
                break
            
            if nums[i] > nums[i-1] and nums[i] > nums[j]:
                count += 1
            elif nums[i] < nums[i-1] and nums[i] < nums[j]:
                count += 1
            
        return count