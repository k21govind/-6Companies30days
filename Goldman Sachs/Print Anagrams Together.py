#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        #Approach :- Sort every word to check angaram and then create a map of the like ones
        
        #code here
        dic={}
        for i in words:
            
            temp="".join(sorted(i))
            if temp in dic:
                dic[temp].append(i)
            else:
              
                #creating dictionary with (key:list of values) pair
                dic[temp]=[i] 
                
        return list(dic.values())
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
