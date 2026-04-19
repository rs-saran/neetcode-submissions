class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()

        if len(s) != len(t):
            return False

        for c in s:
            s_map[c] = s_map.get(c,0) + 1
        
        for c in t:
            s_map[c] = s_map.get(c,0) -1
            if s_map[c] == -1:
                return False
        
        return True
        