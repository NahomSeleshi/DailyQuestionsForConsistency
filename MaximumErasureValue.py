class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniqueElements = set()
        setSum = 0
        answer = float("-inf")
        left = 0
        for each in nums:
            if each in uniqueElements:
                while nums[left] != each:
                    setSum -= nums[left]
                    uniqueElements.remove(nums[left])
                    left += 1
                left += 1
            else:
                setSum += each
                uniqueElements.add(each)
            answer = max(answer, setSum)
        return answer
