class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        sums = 0
        for num in nums:
            sums += num
            temp.append(sums)
        return temp


        