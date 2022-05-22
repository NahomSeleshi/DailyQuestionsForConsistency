class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        charFreq = Counter(s)
        frequency = charFreq[letter]
        percentage = (frequency * 100) // len(s)
        return percentage
