class Solution:
    def concatenatedBinary(self, n: int) -> int:
        decimal_values = []
        for i in range(1,n+1):
            decimal_values.append(bin(i)[2:])
        return int("".join(decimal_values),2)%(10**9+7)