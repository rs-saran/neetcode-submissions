# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        top_k = [[] for _ in range(len(nums))]

        for i in nums:
            counter[i] = counter.get(i,0) + 1

        for f in counter.keys():
            top_k[counter[f]-1].append(f)

        res = []
        # print(top_k)

        for i in range(len(nums)-1,-1,-1):
            l = len(top_k[i])
            res.extend(top_k[i])

            k-=l
            if k<=0:
                return res
        
        return res
            
        

        
        
            
