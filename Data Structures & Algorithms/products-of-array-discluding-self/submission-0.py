class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ansArr = []
        ans = 1

        for i in range(len(nums)):
            ansArr.append(ans)
            ans *= nums[i]

        ans = 1

        for i in range(len(nums) - 1, -1, -1):
            ansArr[i] *= ans
            ans *= nums[i]
        return ansArr