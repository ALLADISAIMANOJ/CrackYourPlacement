class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        res=0
        #First k elements in our window
        for i in range(k):
            res+=cardPoints[i]
        cur=res
        for i in range(k-1,-1,-1):
            #We remove the last visited element and add the non-visited element from the last
            cur-=cardPoints[i]
            cur+=cardPoints[n-k+i]
            #We check the maximum value any possible combination can give
            res=max(res,cur)
        return res



        