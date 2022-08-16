class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1
        charFreq = Counter(s)
        for index, each in enumerate(s):
            if charFreq[each] == 1:
                answer = index
                break
        return answer