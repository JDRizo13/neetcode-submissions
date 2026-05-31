class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a cpunter to see each letter in the word
        arr = []
        
        dictOfwords = {}
        if len(strs) == 1:
            return [strs]
        for word in strs:
            hashedWord = "".join(sorted(word))
            # print(hashedWord)
            if hashedWord not in dictOfwords:
                dictOfwords[hashedWord] = []
            dictOfwords[hashedWord].append(word)
            # print(dictOfwords)
        return list(dictOfwords.values())