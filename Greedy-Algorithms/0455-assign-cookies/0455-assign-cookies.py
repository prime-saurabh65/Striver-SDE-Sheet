'''
    - give each child at most one cookie [give 1 cookie or 0],
    - ans = total children to get cookie assigned
    Approach:
        - sort both 'g' and 's
        - start assigning cookie
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
    
        g.sort()
        s.sort()

        ans = 0

        i, j = 0, 0
        m, n = len(g), len(s)

        while i<m and j<n:
            if s[j] >= g[i]:
                ans += 1
                i+=1
                j+=1
            else:
                j+=1

        return ans