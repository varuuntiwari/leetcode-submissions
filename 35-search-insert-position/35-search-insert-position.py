class Solution:
    def searchInsert(self, nums: List[int], t: int) -> int:
        for i in range(len(nums)):
            if t == nums[i]:
                return i
            if t < nums[i]:
                return i
        
        return len(nums)