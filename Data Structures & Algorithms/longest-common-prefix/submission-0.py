class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         # common = strs[0]
        tempWord = ""
        prefix = strs[0]
        words = list()
        for word in strs:
            for i in range(len(min(word, prefix))):
                if word[i] == prefix[i]:
                    tempWord+=word[i]
                    print(tempWord)
                else:
                    break
            prefix = tempWord
            tempWord = ""
        

        return prefix