#solution 1
#TC: O(2^n), Auxiliary Stack Space O(2^n)
class Solution:  
    #Recursive Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        #here function MaxLoot(n) represents the sum at that index(n) i.e., n
        return self.MaxLoot(a,n-1)
        
    def MaxLoot(self,a,n):
        if n<0:
            return 0
        if n==0:
            return a[0]
        pick=a[n]+self.MaxLoot(a,n-2)
        notpick=self.MaxLoot(a,n-1)
        
        return max(pick, notpick)
            
#Solution 2:
#TC & SC: O(n)
class Solution:  
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        #Here dp[ind] represents the max sum from arr[0] to arr[ind] 
        dp = [-1 for i in range(n)]
        return self.MaxLoot(a,dp,n-1)
        
    def MaxLoot(self,a,dp,ind):
        if ind<0:
            return 0
        if ind==0:
            return a[0]
        if dp[ind]!=-1:
            return dp[ind]
        pick=a[ind]+self.MaxLoot(a,dp,ind-2)
        notpick=self.MaxLoot(a,dp,ind-1)
        
        dp[ind]= max(pick, notpick)
        return dp[ind]
#Solution 3
#Tabulation TC & SC: O(N)
class Solution:
    def FindMaxSum(self,a, n):
        dp=[-1 for i in range(n)]
        dp[0]=a[0]
        for i in range(1, n):
            pick = a[i] if i<2 else a[i]+dp[i-2]
            notpick=dp[i-1]
            dp[i]=max(pick, notpick)
        return dp[n-1]
    
#Solution 4 TC: O(n); SC : O(1)
#Space optimization --Truth of the DP
class Solution:
     def FindMaxSum(self,a, n):
        prev1=a[0]
        for i in range(1, n):
            pick = a[i] if i<2 else a[i]+prev2
            notpick=prev1
            cur=max(pick, notpick)
            prev2=prev1
            prev1=cur
        return prev1



