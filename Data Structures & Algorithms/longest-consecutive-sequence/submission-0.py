class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) == 0:
            return 0
        print(nums)
        start = nums[0]
        
        longest = 1
        current = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1] + 1:
                current += 1

            else:
                longest = max(longest, current)
                current = 1
            
        return max(longest, current)