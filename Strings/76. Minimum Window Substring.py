class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d2={}
        ans=""
        for i in t:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        mcnt=0;dcnt=len(t);d1={};i=-1;j=-1
        while(True):
            #acquire 
            f1=False
            f2=False  
            while(i<len(s)-1 and mcnt<dcnt):
                i+=1
                c=s[i]
                if c not in d1:
                    d1[c]=1
                else:
                    d1[c]+=1
                if d1[c]<=d2.get(c,0):
                    mcnt+=1
                f1=True
            #release
            while j<i and mcnt==dcnt:
                pans=s[j+1:i+1]
                if len(ans)==0 or len(ans)>len(pans):
                    ans=pans[:]
                j+=1
                ch=s[j]
                if d1[ch]==1:
                    d1.pop(ch)
                else:
                    d1[ch]-=1
                if d1.get(ch,0)<d2.get(ch,0):
                    mcnt-=1
                f2=True
            if f1==False and f2==False:
                break
        return ans