class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for c in strs:
            sortedS = ''.join(sorted(c))
            res[sortedS].append(c)
        return list(res.values())