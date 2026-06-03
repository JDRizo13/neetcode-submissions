class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = self.sortArray(nums)

    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]

        leftSorted = self.sortArray(leftHalf)
        rightSorted = self.sortArray(rightHalf)

        result = []
        leftIndex = 0
        rightIndex = 0
        while leftIndex < len(leftSorted) and rightIndex < len(rightSorted):
            if leftSorted[leftIndex] < rightSorted[rightIndex]:
                result.append(leftSorted[leftIndex])
                leftIndex += 1
            else:
                result.append(rightSorted[rightIndex])
                rightIndex += 1
        while leftIndex < len(leftSorted):
            result.append(leftSorted[leftIndex])
            leftIndex += 1
        while rightIndex < len(rightSorted):
            result.append(rightSorted[rightIndex])
            rightIndex += 1
        return result 