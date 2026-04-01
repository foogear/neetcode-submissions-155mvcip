class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0,0,0]
        for i in nums:
            count[i]+=1
        
        index=0
        for i in range(len(count)):
            while count[i]>0:
                nums[index]=i
                count[i]-=1
                index+=1

        