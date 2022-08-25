class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqOfR = Counter(ransomNote)
        freqOfM = Counter(magazine)
        for each in freqOfR:
            if not each in freqOfM or (freqOfR[each] > freqOfM[each]):
                return False
        return True