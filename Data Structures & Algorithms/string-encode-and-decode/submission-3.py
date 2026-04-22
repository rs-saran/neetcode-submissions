# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: dummy_input = ["Hello","World"]

# Output: ["Hello","World"]

# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2

# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:

# Input: dummy_input = [""]

# Output: [""]

# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Follow up: Could you write a generalized algorithm to work on any possible set of characters?

class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for s in strs:
            l = str(len(s))
            enc_str += l
            enc_str += "#" 
            enc_str += s
        
        print(type(enc_str),":",enc_str)
        
        return enc_str


    def decode(self, s: str) -> List[str]:
        dec_strs = []
        enc_str_l = len(s)

        i=0
        while i < enc_str_l:
            j=i
            size = ""
            while s[j] != "#":
                size += s[j]
                j+=1

            l = int(size)
            
            
            if l == 0:
                dec_strs.append("")
            else:
                se = s[j+1:j+l+1]
                dec_strs.append(se)
            i = j+l+1
        
        return dec_strs

