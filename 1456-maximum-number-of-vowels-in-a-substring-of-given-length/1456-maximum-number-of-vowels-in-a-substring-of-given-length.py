class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = k
        n = len(s)
        vowel_count = 0
        max_vowel = 0

        for i in s[0:k]:    #First Window calculation
            if i in 'aeiou':
                vowel_count += 1
                 
        max_vowel = max(max_vowel,vowel_count)

        while r<n:
            if s[l] in 'aeiou':
                vowel_count -= 1
            if s[r] in 'aeiou':
                vowel_count += 1
            
            max_vowel = max(max_vowel,vowel_count)

            l += 1
            r += 1

        return max_vowel