class Solution:
    def isUgly(self, n: int) -> bool:
        def recursively_divide(cur_num):
            if cur_num == 1:
                return True
            two, three, five = False, False, False
            if cur_num % 2 == 0:
                two = recursively_divide(cur_num/2)
            elif cur_num % 3 == 0:
                three = recursively_divide(cur_num/3)
            elif cur_num % 5 == 0:
                five = recursively_divide(cur_num/5)
            return two or three or five
        if n == 0: 
            return False
        return recursively_divide(n)