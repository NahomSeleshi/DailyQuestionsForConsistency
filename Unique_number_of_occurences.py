class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return sorted(list(Counter(arr).values())) == sorted(set(Counter(arr).values()))