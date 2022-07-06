class Solution:
    def fib(self, n: int) -> int:
        fib = [0,1]
        if n == 0: return 0
        if n == 1: return 1
        temp = 2
        while temp <= n:
            currentFib = fib[temp-1] +  fib[temp-2]
            fib.append(currentFib)
            temp += 1
        return fib[-1]
