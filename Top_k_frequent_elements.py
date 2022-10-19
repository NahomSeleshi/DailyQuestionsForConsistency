class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        word_freq = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))
        
        return [word_freq[i][0] for i in range(k)]