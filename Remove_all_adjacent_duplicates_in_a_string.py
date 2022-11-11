class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = []
        for each in s:
            if not char_stack or char_stack[-1] != each:
                char_stack.append(each)
            else:
                while char_stack and char_stack[-1] == each:
                    char_stack.pop()
        
        return "".join(char_stack)
                