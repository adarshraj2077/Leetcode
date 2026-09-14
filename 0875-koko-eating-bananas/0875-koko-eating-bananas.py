class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low<=high:
            k = (low+high) // 2

            total_hours = 0
            
            for pile in piles:
                quotient = pile // k
                remainder = pile % k

                if remainder != 0:
                    quotient += 1

                total_hours = total_hours + quotient

            if total_hours<=h:
                high = k-1
            else:
                low = k+1
        
        return low

