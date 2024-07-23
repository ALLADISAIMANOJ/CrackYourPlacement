class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if nums[abs(i)-1]>0:
                nums[abs(i)-1]=-nums[abs(i)-1]
            else:
                res.append(abs(i))
        return res
