class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for each_word in strs:
            word_dict["".join(sorted(each_word))].append(each_word)
        return list(word_dict.values())