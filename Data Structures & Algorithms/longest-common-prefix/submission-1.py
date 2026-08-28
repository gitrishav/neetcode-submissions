class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        firstWord = strs[0]
        lastWord = strs[-1]
        i = 0
        n = min(len(firstWord), len(lastWord))

        while i < n:
            if firstWord[i] == lastWord[i]:
                i += 1
            else:
                return firstWord[:i]
        return firstWord[:i]            