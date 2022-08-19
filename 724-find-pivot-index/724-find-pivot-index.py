class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sizeArr = len(nums)
        rightSum = 0
        for x in nums:
            rightSum += x

        leftSum = 0
        for i in range(sizeArr):
            if i > 0:
                leftSum += nums[i-1]

            rightSum -= nums[i]
            if leftSum == rightSum:
                return i

        return -1