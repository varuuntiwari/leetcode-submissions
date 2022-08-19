class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in table:
                print(table)
                return [table[comp], i]
            table[nums[i]] = i