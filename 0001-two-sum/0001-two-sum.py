class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        arr = sorted((num, i) for i, num in enumerate(nums))

        i = 0
        j = len(arr) - 1

        while i < j:
            current_sum = arr[i][0] + arr[j][0]

            if current_sum == target:
                return [arr[i][1], arr[j][1]]

            elif current_sum > target:
                j -= 1

            else:
                i += 1