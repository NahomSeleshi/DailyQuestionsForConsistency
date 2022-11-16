class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ""
        t1 = ""
        for i in range(len(s)):
            if s[i] == '#':
                s1 = s1[0:len(s1)-1]
            else:
                s1 += s[i]
        for j in range(len(t)):
            if t[j] == '#':
                t1 = t1[0: len(t1)-1]
            else:
                t1 += t[j]
        if s1 == t1:
            return True
        return False
                
        #H
