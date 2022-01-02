#User function Template for python3


#Approach :- Check if one triangle lies completely to left of the left edge of another triangle or if it lies completely above the another triangle

class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        
        x1=L1[0]
        y1=L1[1]
        x2=R1[0]
        y2=R1[1]#code here
        
        x3=L2[0]
        y3=L2[1]
        x4=R2[0]
        y4=R2[1]
        
        if x2<x3 or x4<x1:
            return 0 
        elif y2>y3 or y4>y1:
            return 0 
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        s=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1],s[0],s[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.doOverlap(p,q,r,s)
        print(ans)
# } Driver Code Ends
