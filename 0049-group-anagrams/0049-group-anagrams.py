class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            key = tuple(sorted(word))   # gives ['a','e','t']

            if key not in seen:
                seen[key] = [word]  # gives ['eat'+ etc.]
            else:
                seen[key].append(word)

        return list(seen.values())