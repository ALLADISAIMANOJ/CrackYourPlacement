#You are given an array a, of n elements. Find the minimum index based distance between two distinct elements of the array, x and y. 
# Return -1, if either x or y does not exist in the array.
# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are two distances between x and y, which are 1 and 3 out of which the least is 1.
#https://www.geeksforgeeks.org/batch/Amazon-Test-Series/track/amazon-arrays/problem/minimum-distance-between-two-numbers

#python code: 
from math import inf
class Solution:
    def minDist(self, arr, n, x, y):
        if n < 2:
            return -1
        if x == y:
            return 0
            
        for left in range(n):
            if arr[left] in {x, y}:
                break
        
        dist = inf
        for right in range(left+1, n):
            if arr[right] in {x,y}:
                if arr[right] != arr[left]:
                    dist = min(dist, abs(right - left))
                left = right
                    
        return dist if dist != inf else -1





#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends