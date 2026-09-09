class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for character in word:
                i = ord(character) - ord("a")
                count[i] += 1
            res[tuple(count)].append(word)
        return list(res.values())