class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        # print(numCount.most_common()[0])
        freqArr = []
        for i in range(k):
            freqArr.append(numCount.most_common()[i][0])
        return freqArr