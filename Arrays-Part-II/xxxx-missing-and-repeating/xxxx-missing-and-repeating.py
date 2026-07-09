class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        # freq dictionary to count frequency of each element
        freq = [0]*(n+1)
        
        duplicate, missing = -1, -1
        
        for i in range(n):
            index = arr[i]
            freq[index] += 1
        
        # Now search for [1, n] and get missing and repeating value:
        for i in range(1, n+1):
            if freq[i] == 0:
                missing = i
            elif freq[i]>1:
                duplicate = i
                
        return [duplicate, missing]