from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        aet: ["eat"]
        """

        # sorted_strs = ["".join(sorted(string)) for string in strs]

        hashmap = defaultdict(list)

        for s in strs:
            hashmap[tuple(sorted(s))].append(s)

        return hashmap.values()
            


        