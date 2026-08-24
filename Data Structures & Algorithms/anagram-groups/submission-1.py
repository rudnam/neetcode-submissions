class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for el in strs:
            sortedEl = "".join(sorted(el))

            if sortedEl not in anagrams:
                anagrams[sortedEl] = [el]
            else:
                anagrams[sortedEl].append(el)
        return anagrams.values()
