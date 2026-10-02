class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            sortedString = str(sorted(string))
            groups[sortedString].append(string)

        return list(groups.values())

        