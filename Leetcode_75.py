class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[1]*len(nums)
        left=0
        right=len(nums)-1
        for items in nums:
            if items==0:
                res[left]=0
                left+=1
                continue
            elif items==2:
                res[right]=2
                right-=1
            else:
                continue
        nums[:]=res
        
