class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        result=[0]*len(nums)

        prefix[0]=1
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        suffix=nums[-1]
        result[-1]=prefix[-1]

        for i in range(len(nums)-2,-1,-1):
            result[i]=suffix*prefix[i]
            suffix=suffix*nums[i]
        return result
