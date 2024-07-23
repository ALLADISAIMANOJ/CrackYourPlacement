class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        n=len(nums)
        for i in range(n):
            if target-nums[i] in hashmap and hashmap[target-nums[i]]!=i:
                return [i,hashmap[target-nums[i]]]
            else:
                hashmap[nums[i]]=i
              