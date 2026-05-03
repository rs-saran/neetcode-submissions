# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        lp = 0

        res_len = float("inf")
        res = "" # [-1,-1]

        t_counter = dict()
        w_counter = dict()

        for c in t:
            t_counter[c] = t_counter.get(c,0) + 1

        req_chars_freq_match = len(t_counter)
        chars_freq_match  = 0

        for rp in range(len(s)):
            # Expand rp until you have all characters (required num of times) once met then collapse lp

            w_counter[s[rp]] = w_counter.get(s[rp],0)+1

            if s[rp] in t_counter and w_counter[s[rp]] == t_counter[s[rp]]:
                chars_freq_match +=1
            
            while req_chars_freq_match == chars_freq_match:
                w_len = rp-lp+1
                
                if w_len < res_len:
                    res_len = w_len
                    res = s[lp:rp+1]

                w_counter[s[lp]] -= 1
                
                if w_counter[s[lp]] < t_counter.get(s[lp],0):
                    chars_freq_match -=1
                
                lp+=1
        return res


        
        