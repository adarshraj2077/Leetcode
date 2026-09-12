class Solution:
    def findMin(self, nums: List[int]) -> int:
        for num in nums:
            num = min(nums)

        return num