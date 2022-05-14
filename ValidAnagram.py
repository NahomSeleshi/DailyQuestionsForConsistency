class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        lettersOfS = Counter(s)
        lettersOfT = Counter(t)
        
        for eachKey in lettersOfS:
            if not eachKey in lettersOfT or lettersOfT[eachKey] != lettersOfS[eachKey]:
                return False
        return True
        
