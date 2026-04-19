class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        n = len(nums)

        pp = [1]*n
        sp = [1]*n

        for i in range(1,n,1):
            pp[i] = pp[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            sp[i] = sp[i+1] * nums[i+1]

        res = []

        for i in range(n):
            res.append(pp[i]*sp[i])

        return res
        