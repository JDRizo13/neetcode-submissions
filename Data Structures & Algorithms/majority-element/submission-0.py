class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityDir = dict()
        counter = 0
        for num in nums:
            if num not in majorityDir:
                counter = 1
                majorityDir[num] = counter
            else: 
                count = majorityDir.get(num)
                count += 1
                majorityDir[num] = count
            # print(majorityDir)
        return max(majorityDir, key=majorityDir.get)