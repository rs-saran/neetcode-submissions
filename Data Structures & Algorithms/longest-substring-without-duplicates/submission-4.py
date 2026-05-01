# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lp = 0
        rp = 0

        hmap =dict()

        max_len = 0

        while rp <  len(s):
            
            if s[rp] in hmap.keys():
                lp = max(lp,hmap[s[rp]] + 1 )
                
            hmap[s[rp]] = rp
            max_len = max(max_len, rp-lp+1)
                
            rp+=1
        
        return max_len




        