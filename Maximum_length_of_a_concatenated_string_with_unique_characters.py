# This is the solution that I found online and I edited it a bit
# This is fast (102ms beats 92.1%)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        all_possibilities = [""]
        max_length = 0
        for word in arr:
            for each in all_possibilities:
                cur_word = word + each
                if len(cur_word) > len(set(cur_word)):
                    continue
                all_possibilities.append(cur_word)
                max_length = max(max_length, len(cur_word))
        return max_length


# This is my first solution and it is slow (2K+ time :) beats 6.5%)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(cur_chars, index):
            cur_chars_copy = cur_chars.copy()
            if index >= len(arr):
                return len(cur_chars)
            dont_take = dfs(cur_chars, index + 1)
            
            for each in arr[index]:
                if each in cur_chars:
                    break
            else:
                cur_chars_copy.update(arr[index])
                
            if len(cur_chars_copy) < len(cur_chars) + len(arr[index]):
                take = dfs(cur_chars, index + 1)
            else:
                take = dfs(cur_chars_copy, index + 1)
            return max(take, dont_take)
        
        cur_values = set()
        return dfs(cur_values, 0)
            
            
            