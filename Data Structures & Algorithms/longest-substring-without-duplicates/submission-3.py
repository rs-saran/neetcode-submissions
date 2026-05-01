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
        # if len(s) in (0,1):
        #     return len(s)

        while rp <  len(s):
            # print(s[lp:rp+1], rp+1-lp)
            if s[rp] in hmap.keys():
                # max_len = max(max_len, rp-lp)
                if lp > hmap[s[rp]]:
                    max_len = max(max_len, rp-lp+1)
                else:
                    lp = hmap[s[rp]] + 1
                # lp = max(lp,hmap[s[rp]] + 1)
                hmap[s[rp]] = rp

            else:
                hmap[s[rp]] = rp
                max_len = max(max_len, rp-lp+1)
                
            rp+=1
        
        return max_len




        