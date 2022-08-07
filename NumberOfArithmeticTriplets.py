class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        leftSet = set(nums[0:1])
        rightSet = set(nums[1:])
        answer = 0
        visitedTriplets = set()
        for i in range(1,len(nums)-1):
            if nums[i] in visitedTriplets: 
                continue
            if nums[i]-diff in leftSet and nums[i] + diff in rightSet:
                answer += 1
                visitedTriplets.add(nums[i])
            leftSet.add(nums[i])
            rightSet.remove(nums[i])
        return answer