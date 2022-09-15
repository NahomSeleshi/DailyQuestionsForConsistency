class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        numFreq = Counter(changed)
        if numFreq[0] % 2:
            return []
        for each in sorted(numFreq):
            if numFreq[each] > numFreq[each*2]:
                return []
            numFreq[each*2] -= numFreq[each] if each else numFreq[each]//2
        return list(numFreq.elements())