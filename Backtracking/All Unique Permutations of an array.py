#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        ds = []
        visited = [0] * n
        ans = []
        arr.sort()  # Sort the array to handle duplicates
        self.permutate(arr, ds, visited, ans)
        return ans
    
    def permutate(self, arr, ds, visited, ans):
        if len(ds) == len(arr):
            ans.append(ds.copy())
            return
        used = set()  # Set to keep track of elements used in the current position
        for i in range(len(arr)):
            if visited[i] == 0 and arr[i] not in used:
                visited[i] = 1
                ds.append(arr[i])
                self.permutate(arr, ds, visited, ans)
                visited[i] = 0
                ds.pop()
                used.add(arr[i])  # Add element to the set after exploring its permutations

                
                
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends