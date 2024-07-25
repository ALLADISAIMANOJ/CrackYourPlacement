#User function Template for python3
class Solution:
    def maxIndexDiff(self, arr):
        n=len(arr)
        Rmax=[-1]*n
        maxele=0
        for i in range(n-1,-1,-1):
            if maxele<arr[i]:
                maxele=arr[i]
            Rmax[i]=maxele
        
        maxDist = -2**31
        i = 0
        j = 0
         
        while (i < n and j < n):
            if (Rmax[j] >= arr[i]):
                maxDist = max(maxDist, j - i)
                j += 1
                 
            else:
                # if(rightMax[j] < leftMin[i]) 
                i += 1
         
        return maxDist
        #[34, 8, 10, 3, 2, 80, 30, 33, 1]
        #[80, 80, 80, 80, 80, 80, 33, 33, 1]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxIndexDiff(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends