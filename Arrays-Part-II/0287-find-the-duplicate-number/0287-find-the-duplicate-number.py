class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Applying Binary Seach on Answers:

        def helper(num):
            count = 0
            for i in range(n):
                if nums[i] <= num:
                    count += 1
            return count > num


        n = len(nums)

        left, right = 1, n
        ans = -1

        while left<=right:
            mid = (left+right)//2

            if helper(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans