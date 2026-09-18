class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        seen = set()
        max_count = 0
        left = 0
        
        for char in s:
            if char not in seen:
                seen.add(char)
                count += 1
            
                max_count = max(max_count,count)
            else:
                while char in seen:
                    left_char = s[left]
                    seen.remove(left_char)
                    left += 1
                    count -= 1
                    
                seen.add(char)
                count += 1
                max_count = max(max_count,count)
        
        return max_count