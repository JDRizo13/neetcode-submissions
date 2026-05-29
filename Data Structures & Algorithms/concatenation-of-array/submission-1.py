class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copyNums = nums.copy()
        for num in nums:
            copyNums.append(num)
        return copyNums
        