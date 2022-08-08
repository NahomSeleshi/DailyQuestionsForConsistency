class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stoneFreq = Counter(stones)
        answer = 0
        for each in jewels:
            answer += stoneFreq[each]
        return answer