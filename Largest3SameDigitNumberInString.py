class Solution:
    def largestGoodInteger(self, num: str) -> str:
        goodDigits = set()
        goodInNum = []
        answer = ""
        for i in range(10):
            temp = str(i)
            temp = temp+temp+temp
            goodDigits.add(temp)
        for i in range(len(num)-2):
            if num[i:i+3] in goodDigits:
                goodInNum.append(num[i:i+3])
        if goodInNum:
            answer = goodInNum[0]
            for each in goodInNum:
                if int(each) > int(answer):
                    answer = each
            return answer
        return ""
        
