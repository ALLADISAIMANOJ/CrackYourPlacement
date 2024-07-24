# Brute Force Solution
# TC: O(N^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        ans=[nums[i],nums[j],nums[k]]
                        ans.sort()
                        result.add(tuple(ans))
        return list(result)

#Better Solution --> TC:O(N^3) & SC:O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=nums
        n=len(nums)
        st = set()
        for i in range(n):
            hashset = set()
            for j in range(i + 1, n):
                # Calculate the 3rd element:
                third = -(arr[i] + arr[j])

                # Find the element in the set:
                if third in hashset:
                    temp = [arr[i], arr[j], third]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(arr[j])

        # store the set in the answer:
        ans = list(st)
        return ans
    
#Best Optimal Solution --> 3 pointer approach TC: O(nlogn)(for sorting) +o(n)(for traversing)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while(l<r):
                threeSum=a+nums[l]+nums[r]
                if(threeSum>0):
                    r-=1
                elif(threeSum<0):
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l < r :
                        l+=1
        return res
        