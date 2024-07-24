
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        prefixsum=0
        cnt=0
        hashmap[0]=1
        for i in nums:
            prefixsum+=i
            remove=prefixsum-k
            cnt+=hashmap[remove]
            hashmap[prefixsum]+=1
        return cnt