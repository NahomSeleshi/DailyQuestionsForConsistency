class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        i = 0
        while num:
            answer += (num // integers[i]) * romans[i]
            num %= integers[i]
            i += 1 
        return answer
        
