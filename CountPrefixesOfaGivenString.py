class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        canBePrefix = False
        for string in words:
            for i in range(len(string)):
                if i >= len(s):
                    canBePrefix = False
                    break
                if string[i] == s[i]:
                    canBePrefix = True
                else:
                    canBePrefix = False
                    break
            if canBePrefix:
                count += 1
            canBePrefix = False
        return count
        
