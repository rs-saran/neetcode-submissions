class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hmap = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            hmap[key].append(s)

        return list(hmap.values())