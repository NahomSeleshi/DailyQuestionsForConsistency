class Solution:
    def minDeletions(self, s: str) -> int:
        charFreq = Counter(s)
        minimumDeletion, uniqueFreq = 0, set()
        
        for eachKey in charFreq:
            tempFreq = charFreq[eachKey]
            if tempFreq in uniqueFreq:
                while tempFreq > 0 and tempFreq in uniqueFreq:
                    tempFreq -= 1
                    minimumDeletion += 1
            uniqueFreq.add(tempFreq)
        
        return minimumDeletion
