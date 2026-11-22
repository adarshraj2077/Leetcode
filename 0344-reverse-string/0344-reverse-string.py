class Solution:
    def reverseString(self, s: List[str],i=0,j=None) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if j == None:
            j = len(s)-1

        if i>j:
            return

        s[i],s[j] = s[j],s[i]
        
        self.reverseString(s,i+1,j-1)