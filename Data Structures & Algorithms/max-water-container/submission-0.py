# You are given an integer array heights where heights[i] represents the height of the 
# i
# t
# h
# i 
# th
#   bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4
# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights)-1
        max_water = 0
        
        # water formula = (rp-lp) * min(heights[lp],heights[rp])
        while lp < rp:
            if heights[lp] <= heights[rp]:
                water  = (rp-lp) * heights[lp] 
                lp+=1 # only change the pointer which has min height (as formula is dependent on only min of heights at lp,rp)
            else:
                water = (rp-lp) * heights[rp] 
                rp-=1
            
            if max_water < water:
                max_water = water

        return max_water


        