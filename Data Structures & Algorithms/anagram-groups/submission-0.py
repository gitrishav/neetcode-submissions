class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            idCard = "".join(sorted(word))

            if idCard in seen:
                seen[idCard].append(word)
            else:
                seen[idCard] = [word]
        return list(seen.values()) 