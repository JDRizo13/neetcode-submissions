class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        filteredNums = list(filter(lambda x: x > 0, nums))
        sortedNums = sorted(set(filteredNums))
        # print(sortedNums)
        if len(sortedNums) == 0:
            return 1

        follow = 1
        for i in range(len(sortedNums)):
            if sortedNums[i] != follow:
                return follow
            follow += 1
        return follow
        