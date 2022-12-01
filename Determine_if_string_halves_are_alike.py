class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left_count, right_count = 0,0
        for i in range(n):
            if i < n/2 and s[i] in vowels:
                left_count += 1
            elif i >= n/2 and s[i] in vowels:
                right_count += 1
        return left_count == right_count