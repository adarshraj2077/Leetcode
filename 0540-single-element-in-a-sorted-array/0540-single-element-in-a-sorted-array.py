class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while low<high:
            mid = (low+high) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    low = mid + 2
                else:
                    if nums[mid-1] == nums[mid]:
                        high = mid - 1
                    else:
                        return nums[mid]
            
            if mid % 2 != 0:
                if nums[mid-1] == nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return nums[low]