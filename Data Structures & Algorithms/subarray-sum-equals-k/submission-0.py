class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        currSum = 0
        seen = {0: 1}
        for num in nums:
            currSum += num
            if currSum - k in seen:
                counter += seen[currSum - k]
            if currSum not in seen:
                seen[currSum] = 0
            seen[currSum] += 1
        return counter
        