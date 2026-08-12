class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=nums[0]
        sub_sum=nums[0]

        for i in range(1,len(nums)):
            currsum=max(nums[i],currsum+nums[i])
            sub_sum=max(currsum,sub_sum)
        return sub_sum

        