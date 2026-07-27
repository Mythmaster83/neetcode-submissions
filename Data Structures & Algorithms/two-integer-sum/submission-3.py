class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind1 = 0
        for i in range(len(nums)):
            need = target - nums[i]
            if need in nums[i+1:]:
                ind1 = i 
                break
        return [ind1, nums[ind1+1:].index(need) + (ind1 + 1)]