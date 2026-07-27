class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        for i in range(len(ans)):
            for g in range(len(nums)):
                if g == i:
                    pass
                else:
                    ans[i] *= nums[g]
        return ans