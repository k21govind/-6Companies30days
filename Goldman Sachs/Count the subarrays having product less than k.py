#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        
        #Code here
        
        
        
        """
        This approach gives TLE
        l=0
        r=0
        prod=1
        c=0
        while l<n and r<n:
            prod*=a[r]
            
            if prod<k:
                
                #print(a[l:r+1])
                #print(prod)
                c+=1 
                r+=1 
                if r==n and l!=n:
                    l+=1 
                    r=l
                    prod=1 
            else:
                l+=1 
                r=l 
                prod=1 
                
        return c"""
        
        
        
        
        #Optimized Approach :- Using sliding window technique
        
        start=0
        prod=1
        count=0
        
        for end in range(n):
            prod*=a[end]
            while start<end and prod>=k:
                prod//=a[start]
                start+=1 
                
            if prod<k:
              
                #subcount is equal to the length of the window
                subcount=end-start+1 
                count+=subcount 
        return count
                
        
        
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()
