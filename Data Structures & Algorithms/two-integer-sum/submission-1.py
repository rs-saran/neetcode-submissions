class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        le = len(nums)
        for i in range(0,le-1):
            for j in range(i+1,le):
                if target == nums[i] + nums[j]:
                    return [i,j]



        