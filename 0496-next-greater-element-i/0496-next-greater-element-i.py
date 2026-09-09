class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                stack.append(nums2[i])
                next_greater[nums2[i]] = -1
            else:
                while stack and nums2[i] > stack[-1]:
                    stack.pop() 
                
                if not stack:
                    next_greater[nums2[i]] = -1
                else:
                    next_greater[nums2[i]] = stack[-1]

                stack.append(nums2[i])
        
        ans = []

        for num in nums1:
            ans.append(next_greater[num])
            
        return ans
        