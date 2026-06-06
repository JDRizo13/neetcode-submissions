class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        keys = list(count.keys())
        majority = []
        for key in keys:
            if count.get(key) > (len(nums)/3):
                majority.append(key)
        return majority
        