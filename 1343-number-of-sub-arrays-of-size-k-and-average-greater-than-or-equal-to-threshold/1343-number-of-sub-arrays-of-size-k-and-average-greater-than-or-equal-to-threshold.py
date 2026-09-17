class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        l = 0
        r = k
        count = 0

        sum_arr = sum(arr[l:r])

        while r < n:
            if (sum_arr)/k >= threshold:
                count += 1

            sum_arr = sum_arr - arr[l] + arr[r]
            l += 1
            r += 1
        
        if (sum_arr)/k >= threshold:
            count += 1

        return count