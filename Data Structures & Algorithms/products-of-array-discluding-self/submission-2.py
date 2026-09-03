class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            pre *= nums[i-1]
            prefix[i] = pre
        post = 1
        postfix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            post *= nums[i+1]
            postfix[i] = post
        return [prefix[i] * postfix[i] for i in range(len(nums))]