# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Constraints:

# 1 <= s.length <= 1000
# 0 <= k <= s.length
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hmap = dict()

        lp = 0
        max_len = 0
        max_count = 0

        for rp in range(len(s)):
            hmap[s[rp]] = hmap.get(s[rp],0) + 1
            max_count = max(max_count,hmap[s[rp]])

            # Num of max replacements needed in a window = window_size - max_freq of a char
            
            while (rp-lp+1) - max_count > k:
                hmap[s[lp]] -= 1
                lp+=1
            
            max_len = max(max_len,rp-lp+1)

        return max_len

