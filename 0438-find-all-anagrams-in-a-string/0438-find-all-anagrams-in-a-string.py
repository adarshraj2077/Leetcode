class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        seen = {}
        window_freq = {}

        window = len(p)
        left = 0
        right = 0
        result = []

        for char in p:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1

        while right < len(s):

            if s[right] not in window_freq:
                window_freq[s[right]] = 1
            else:
                window_freq[s[right]] += 1

            if right - left + 1 > window:
                window_freq[s[left]] -= 1

                if window_freq[s[left]] == 0:
                    del window_freq[s[left]]

                left += 1

            if right - left + 1 == window:
                if window_freq == seen:
                    result.append(left)

            right += 1

        return result