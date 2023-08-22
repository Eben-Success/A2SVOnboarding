from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        aet: ["eat"]
        """

        sorted_strs = ["".join(sorted(string)) for string in strs]

        hashmap = defaultdict(list)

        for i in range(len(strs)):
            hashmap[sorted_strs[i]].append(strs[i])

        return list(hashmap.values())
            


        