class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=[]
        arr.append(nums[0])

        for i in range(1,len(nums)):
            if arr[i-1]>0:
                arr.append(arr[i-1]+nums[i])
            else:
                arr.append(nums[i])
        return max(arr)
