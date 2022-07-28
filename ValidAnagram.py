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
        
#Another implementaion somehow similar to the one above
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqOfS = Counter(s)
        freqOfT = Counter(t)
        for each in freqOfS:
            if not freqOfS[each] == freqOfT[each]:
                return False
        for each in freqOfT:
            if not freqOfS[each] == freqOfT[each]:
                return False
        return True
#Another different implementation
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        if len(s) != len(t): return False
        for i in range(len(s)):
            if s[i] != t[i]: return False
        return True
