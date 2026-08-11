class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
            
        var = x
        result = 0

        while var>0:
            ld = var % 10
            result = result * 10 + ld
            var = var // 10
    
        return x == result